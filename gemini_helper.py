from transformers import AutoTokenizer
from transformers import AutoModelForSeq2SeqLM

MODEL_NAME = "google/flan-t5-base"

print("Loading AI model...")

tokenizer = AutoTokenizer.from_pretrained(
    MODEL_NAME
)

model = AutoModelForSeq2SeqLM.from_pretrained(
    MODEL_NAME
)

print("Model loaded successfully")


def generate_response(prompt):

    try:

        formatted_prompt = f"""
        Answer the following question clearly and in simple language:

        {prompt}
        """

        inputs = tokenizer(
            formatted_prompt,
            return_tensors="pt",
            truncation=True,
            max_length=512
        )

        outputs = model.generate(
            **inputs,
            max_new_tokens=300,
            temperature=0.7,
            do_sample=True
        )

        response = tokenizer.decode(
            outputs[0],
            skip_special_tokens=True
        )

        return response

    except Exception as e:

        return f"Error: {str(e)}"