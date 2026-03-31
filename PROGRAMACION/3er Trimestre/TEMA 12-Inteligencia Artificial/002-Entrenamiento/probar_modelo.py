import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel

# 1. Define las rutas
# OJO: Cambia esto por el nombre exacto del modelo base que descargaste de HuggingFace al entrenar
base_model_name = "Qwen/Qwen2.5-0.5B" 
adapter_path = "./qwen25-05b-jvc"

print("Cargando tokenizador...")
tokenizer = AutoTokenizer.from_pretrained(adapter_path)

print("Cargando modelo base...")
base_model = AutoModelForCausalLM.from_pretrained(
    base_model_name,
    torch_dtype=torch.float16, # Usa float16 o bfloat16 para ahorrar memoria
    device_map="auto" # Carga automáticamente en GPU si está disponible
)

print("Aplicando los pesos de LoRA...")
model = PeftModel.from_pretrained(base_model, adapter_path)
model.eval() # Ponemos el modelo en modo evaluación

# 2. Preparamos una pregunta (Inferencia)
pregunta = "¿Qué son las variables en programación?"

# Usamos el formato de chat (clave si en el log usaste "chat-style text")
messages = [
    {"role": "user", "content": pregunta}
]

# Aplicamos la plantilla del modelo
text_input = tokenizer.apply_chat_template(
    messages, 
    tokenize=False, 
    add_generation_prompt=True
)

print("\nGenerando respuesta...")
inputs = tokenizer(text_input, return_tensors="pt").to(model.device)

# 3. Generar la respuesta
with torch.no_grad():
    outputs = model.generate(
        **inputs,
        max_new_tokens=200,     # Límite de palabras de la respuesta
        temperature=0.7,        # Grado de creatividad (0.1 muy estricto, 0.9 creativo)
        top_p=0.9,
        do_sample=True,
        pad_token_id=tokenizer.eos_token_id
    )

# 4. Decodificar y mostrar el resultado
# Recortamos el input de la salida para ver solo la respuesta nueva
input_length = inputs["input_ids"].shape[1]
response_tokens = outputs[0][input_length:]
respuesta_final = tokenizer.decode(response_tokens, skip_special_tokens=True)

print("\n--- RESPUESTA ---")
print(respuesta_final)