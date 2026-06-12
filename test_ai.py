from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "google/flan-t5-base"

print("Loading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(model_name)

print("Loading model...")
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

prompt = "Explain Artificial Intelligence in simple words."

inputs = tokenizer(
    prompt,
    return_tensors="pt"
)

outputs = model.generate(
    **inputs,
    max_new_tokens=100
)

result = tokenizer.decode(
    outputs[0],
    skip_special_tokens=True
)

print("\nResult:")
print(result)