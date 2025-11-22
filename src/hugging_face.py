from transformers import pipeline

# Load a small text generation model from Hugging Face
generator = pipeline("text-generation", model="distilgpt2")

# Ask the model "How does AI work?"
prompt = "How does AI work?"
response = generator(prompt, max_length=50, num_return_sequences=1)

# Print the response
print(response[0]['generated_text'])