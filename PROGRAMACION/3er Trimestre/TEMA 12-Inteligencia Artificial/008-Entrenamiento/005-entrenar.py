#!/usr/bin/env python3
import os
import torch
from datetime import datetime

from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForCausalLM, Trainer, TrainingArguments
from peft import LoraConfig, get_peft_model


# ------------------------------------------------------------
# CONFIG (simplificado)
# ------------------------------------------------------------
DATA_FILE = "004-preentrenamiento relleno.jsonl"
MODEL_NAME = "Qwen/Qwen2.5-3B-Instruct"
OUTPUT_DIR = "./qwen25-3b-jvc-lora"

MAX_LENGTH = 512
NUM_EPOCHS = 3
LR = 2e-4
BATCH_SIZE = 1
GRAD_ACCUM = 4


def main():
    start_dt = datetime.now()

    if not os.path.isfile(DATA_FILE):
        raise FileNotFoundError(f"No existe el fichero de entrenamiento: {DATA_FILE}")

    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"🚀 Training: {MODEL_NAME}")
    print(f"📄 Data file: {DATA_FILE}")
    print(f"💻 Device: {device}")
    print("-" * 60)

    # ------------------------------------------------------------
    # Load dataset
    # ------------------------------------------------------------
    raw_dataset = load_dataset(
        "json",
        data_files=DATA_FILE,
        split="train",
    )
    print(f"✅ Dataset loaded: {len(raw_dataset)} examples")

    # ------------------------------------------------------------
    # Tokenizer + model
    # ------------------------------------------------------------
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, use_fast=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        device_map="auto" if device == "cuda" else None,
    )
    if device == "cpu":
        model.to(device)

    # ------------------------------------------------------------
    # LoRA
    # ------------------------------------------------------------
    lora_config = LoraConfig(
        r=8,
        lora_alpha=16,
        target_modules=["q_proj", "k_proj", "v_proj", "o_proj",
                        "gate_proj", "up_proj", "down_proj"],
        lora_dropout=0.05,
        bias="none",
        task_type="CAUSAL_LM",
    )
    model = get_peft_model(model, lora_config)
    model.print_trainable_parameters()

    # ------------------------------------------------------------
    # Q/A -> chat text
    # ------------------------------------------------------------
    SYSTEM_PROMPT = (
        "Eres un asistente educativo en español que responde de forma clara, "
        "precisa y concisa a preguntas técnicas."
    )

    def qa_to_text(example):
        q = example.get("question", "")
        a = example.get("answer", "")
        if not isinstance(q, str):
            q = str(q)
        if not isinstance(a, str):
            a = str(a)

        conv = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": q},
            {"role": "assistant", "content": a},
        ]

        # Qwen Instruct soporta chat template (normalmente)
        text = tokenizer.apply_chat_template(
            conv,
            tokenize=False,
            add_generation_prompt=False,
        )
        return {"text": text}

    text_dataset = raw_dataset.map(qa_to_text)

    # ------------------------------------------------------------
    # Tokenize
    # ------------------------------------------------------------
    def tokenize_fn(batch):
        out = tokenizer(
            batch["text"],
            truncation=True,
            max_length=MAX_LENGTH,
            padding="max_length",
        )
        out["labels"] = out["input_ids"].copy()
        return out

    tokenized_dataset = text_dataset.map(
        tokenize_fn,
        batched=True,
        remove_columns=text_dataset.column_names,
    )

    # ------------------------------------------------------------
    # TrainingArguments
    # ------------------------------------------------------------
    training_args = TrainingArguments(
        output_dir=OUTPUT_DIR,
        overwrite_output_dir=True,
        num_train_epochs=NUM_EPOCHS,
        per_device_train_batch_size=BATCH_SIZE,
        gradient_accumulation_steps=GRAD_ACCUM,
        learning_rate=LR,
        weight_decay=0.01,
        warmup_ratio=0.03,
        logging_steps=10,
        save_steps=200,
        save_total_limit=1,
        fp16=(device == "cuda"),
        bf16=False,
        dataloader_pin_memory=False,
        report_to="none",
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_dataset,
    )

    # ------------------------------------------------------------
    # Train + save
    # ------------------------------------------------------------
    print("🚂 Training...")
    train_output = trainer.train()
    print("🏁 Done.")

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    trainer.save_model(OUTPUT_DIR)
    tokenizer.save_pretrained(OUTPUT_DIR)

    end_dt = datetime.now()
    metrics = getattr(train_output, "metrics", None) or {}
    print(f"✅ Saved to: {OUTPUT_DIR}")
    print(f"⏱️ Duration: {end_dt - start_dt}")
    if metrics:
        print("📊 Metrics:", metrics)


if __name__ == "__main__":
    main()
