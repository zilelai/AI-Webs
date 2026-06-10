import json
import urllib.request
import urllib.error
import time


API_KEY = "AQ.Ab8RN6IZvqv9EdjrcUuZhG7x-X_V1gx_0z6wHEVT35ZWbJuFoQ"


MODEL = "gemini-2.5-flash"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}"

print("Ask Gemini\n")


while True:
    try:

        user_prompt = input("\nYou: ")
        

        if user_prompt.lower() in ['exit', 'quit']:
            print("See you again!")
            break
            

        if not user_prompt.strip():
            continue

        payload = {
            "contents": [{"parts": [{"text": user_prompt}]}]
        }

        json_data = json.dumps(payload).encode("utf-8")

        req = urllib.request.Request(
            URL,
            data=json_data,
            headers={"Content-Type": "application/json"},
            method="POST"
        )

        print("Gemini is thinking...")

        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode("utf-8"))

            print(f"\nGemini: {result['candidates'][0]['content']['parts'][0]['text']}")

    except urllib.error.HTTPError as e:
        
        if e.code == 429:
            print("\nSYSTEM OVERLOAD!!!")
            time.sleep(5)
        else:
            print(f"\nHTTP Error {e.code}: {e.reason}")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
