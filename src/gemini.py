from google import genai

client = genai.Client(api_key="AIzaSyAj7YuNsytn5vwePBQBWyus9k855_ZRG3c")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain how AI works in a few words",
)

print(response.text)