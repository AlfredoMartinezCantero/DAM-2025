#!/usr/bin/env python3
import os
import json
import torch
import platform
import glob
from datetime import datetime

from datasets import load_dataset
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    Trainer,
    TrainingArguments,
    DataCollatorForLanguageModeling
)
from peft import (
    LoraConfig,
    get_peft_model,
    prepare_model_for_kbit_training
)

# -------------------------------------------------------------------
# CONFIG
# -------------------------------------------------------------------

DATA_PATH = "outputs/*.jsonl" 

# Cambio a Qwen2.5-Coder-7B
MODEL_NAME = "Qwen/Qwen2.5-Coder-7B-Instruct"
OUTPUT_DIR = "./qwen25-coder-7b-jvc"

MAX_LENGTH = 512
NUM_EPOCHS = 3
LR = 2e-4
BATCH_SIZE = 1  # Mantener bajo para 7B
GRAD_ACCUM = 8  # Aumentado para compensar el batch size pequeño


# -------------------------------------------------------------------
# REPORTING
# -------------------------------------------------------------------

def generate_markdown_report(
    *,
    start_dt: datetime,
    end_dt: datetime,
    device: str,
    data_path_pattern: str,
    jsonl_files,
    dataset_size: int,
    training_args: TrainingArguments,
    train_metrics: dict | None,
) -> str:
    duration = end_dt - start_dt
    epoch = int(end_dt.timestamp())
    timestamp_str = end_dt.strftime("%Y%m%d_%H%M%S")
    report_name = f"reporte_entrenamiento_{timestamp_str}_{epoch}.md"
    report_path = os.path.join(OUTPUT_DIR, report_name)

    system_info = {
        "Sistema operativo": platform.system(),
        "Python": platform.python_version(),
        "PyTorch": torch.__version__,
        "CUDA disponible": torch.cuda.is_available(),
        "Dispositivo de entrenamiento": device,
    }

    per_file_counts = []
    total_lines = 0
    for path in sorted(jsonl_files):
        count = 0
        try:
            with open(path, "r", encoding="utf-8") as f:
                for line in f:
                    if line.strip(): count += 1
        except Exception as e:
            per_file_counts.append({"file": path, "count": None, "error": str(e)})
            continue
        per_file_counts.append({"file": path, "count": count, "error": None})
        total_lines += count

    lines = [
        "# Informe de entrenamiento Qwen2.5-Coder\n",
        "## Resumen\n",
        f"- **Modelo base:** `{MODEL_NAME}`",
        f"- **Duración:** {duration}",
        f"- **Total ejemplos:** {dataset_size}",
        f"- **Dispositivo:** {device}\n",
        "## Parámetros\n",
        f"- **LR:** {LR}, **Epochs:** {NUM_EPOCHS}, **Max Length:** {MAX_LENGTH}\n",
        "## Métricas\n"
    ]
    
    if train_metrics:
        for k, v in train_metrics.items(): lines.append(f"- **{k}:** {v}")
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"📝 Informe generado en: {report_path}")
    return report_path


# -------------------------------------------------------------------
# MAIN
# -------------------------------------------------------------------

def main():
    start_dt = datetime.now()

    print(f"🚀 Starting Qwen2.5-Coder-7B training")
    
    # -------------------------------------------------------------------
    # Check Files
    # -------------------------------------------------------------------
    jsonl_files = glob.glob(DATA_PATH)
    if not jsonl_files:
        raise FileNotFoundError(f"No se encontraron archivos en {DATA_PATH}")

    # -------------------------------------------------------------------
    # Device & Precision
    # -------------------------------------------------------------------
    if torch.cuda.is_available():
        device = "cuda"
        # Usar bfloat16 si está disponible (A100/H100/30xx/40xx), si no float16
        compute_dtype = torch.bfloat16 if torch.cuda.is_bf16_supported() else torch.float16
        print(f"💻 CUDA detectado. Usando precisión: {compute_dtype}")
    else:
        device = "cpu"
        compute_dtype = torch.float32
        print("💻 Entrenando en CPU (Extremadamente lento para 7B)")

    # -------------------------------------------------------------------
    # Load Model & Tokenizer
    # -------------------------------------------------------------------
    print("✅ Loading tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    print("✅ Loading model (7B version)...")
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        torch_dtype=compute_dtype,
        device_map="auto" if device == "cuda" else None,
        trust_remote_code=True
    )

    # -------------------------------------------------------------------
    # LoRA Config
    # -------------------------------------------------------------------
    print("✅ Configuring LoRA...")
    lora_config = LoraConfig(
        r=16, # Un poco más de rango para un modelo más grande
        lora_alpha=32,
        target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],
        lora_dropout=0.05,
        bias="none",
        task_type="CAUSAL_LM",
    )
    
    model = get_peft_model(model, lora_config)
    # Importante: Para modelos grandes, habilitar checkpointing ahorra mucha VRAM
    model.gradient_checkpointing_enable() 
    model.print_trainable_parameters()

    # -------------------------------------------------------------------
    # Dataset Processing
    # -------------------------------------------------------------------
    raw_dataset = load_dataset("json", data_files=DATA_PATH, split="train")

    def format_instruction(example):
        # Qwen2.5-Coder utiliza el formato ChatML
        messages = [
            {"role": "system", "content": "Eres un experto programador y asistente técnico."},
            {"role": "user", "content": str(example.get("question", ""))},
            {"role": "assistant", "content": str(example.get("answer", ""))}
        ]
        return {"text": tokenizer.apply_chat_template(messages, tokenize=False)}

    print("🧱 Formatting dataset...")
    formatted_dataset = raw_dataset.map(format_instruction)

    def tokenize_fn(batch):
        return tokenizer(
            batch["text"],
            truncation=True,
            max_length=MAX_LENGTH,
            padding=False, # El collator se encargará del padding dinámico
        )

    print("✅ Tokenizing...")
    tokenized_dataset = formatted_dataset.map(
        tokenize_fn,
        batched=True,
        remove_columns=raw_dataset.column_names + ["text"]
    )

    # -------------------------------------------------------------------
    # Training
    # -------------------------------------------------------------------
    training_args = TrainingArguments(
        output_dir=OUTPUT_DIR,
        overwrite_output_dir=True,
        num_train_epochs=NUM_EPOCHS,
        per_device_train_batch_size=BATCH_SIZE,
        gradient_accumulation_steps=GRAD_ACCUM,
        learning_rate=LR,
        weight_decay=0.01,
        logging_steps=5,
        save_total_limit=1,
        fp16=(device == "cuda" and compute_dtype == torch.float16),
        bf16=(device == "cuda" and compute_dtype == torch.bfloat16),
        gradient_checkpointing=True, # Crucial para 7B
        report_to="none",
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_dataset,
        data_collator=DataCollatorForLanguageModeling(tokenizer, mlm=False),
    )

    print("🚂 Starting training...")
    train_output = trainer.train()

    # -------------------------------------------------------------------
    # Finalize
    # -------------------------------------------------------------------
    print(f"💾 Saving to {OUTPUT_DIR}")
    trainer.save_model(OUTPUT_DIR)
    tokenizer.save_pretrained(OUTPUT_DIR)

    generate_markdown_report(
        start_dt=start_dt,
        end_dt=datetime.now(),
        device=device,
        data_path_pattern=DATA_PATH,
        jsonl_files=jsonl_files,
        dataset_size=len(raw_dataset),
        training_args=training_args,
        train_metrics=train_output.metrics if train_output else None,
    )

if __name__ == "__main__":
    main()