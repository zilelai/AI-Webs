import json
import urllib.request
import urllib.error
import time


API_KEY = "-"


URL = "https://api.groq.com/openai/v1/chat/completions"

MODEL = "meta-llama/llama-4-scout-17b-16e-instruct"

print(f"Meta Llama 4 ({MODEL}) on Groq!\n")

while True:
    try:
        user_prompt = input("\nYou: ")
        
        if user_prompt.lower() in ['exit', 'quit']:
            print("See you again!")
            break
            
        if not user_prompt.strip():
            continue

        payload = {
            "model": MODEL,
            "messages": [
                {"role": "user", "content": user_prompt}
            ],
            "temperature": 0.6
        }

        json_data = json.dumps(payload).encode("utf-8")


        req = urllib.request.Request(
            URL,
            data=json_data,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {API_KEY}",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                "Accept": "application/json",
                "Accept-Language": "en-US,en;q=0.9"
            },
            method="POST"
        )

        print("Thinking...")

        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode("utf-8"))
            reply = result["choices"][0]["message"]["content"]
            print(f"\nMeta LLama 4: {reply}")

    except urllib.error.HTTPError as e:
        error_msg = e.read().decode('utf-8')
        print(f"\nHTTP Error {e.code}: {error_msg}")
        if e.code == 429:
            time.sleep(5)
    except Exception as e:
        print(f"\nAn error occurred: {e}")
