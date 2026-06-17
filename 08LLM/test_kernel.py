from google import genai
import os

GEMINI_API_KEY = 'REDACTED_GCP_KEY'

try:
    print("Initializing client...")
    client = genai.Client(api_key=GEMINI_API_KEY)
    
    print("Attempting to generate content with gemini-1.5-flash (safe model)...")
    # Using a known good model name to see if it's a library issue or model name issue
    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents="Hello"
    )
    print("Response received:")
    print(response.text)
except Exception as e:
    print(f"Caught exception: {e}")
