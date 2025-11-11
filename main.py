import os
import sys
from google import genai
from dotenv import load_dotenv

def main(args):
    if len(args) < 2:
        print("WARNING: no prompt supplied to agent")
        sys.exit(1)

    verbose_enabled = False
    for i in range(2, len(args)):
        if sys.argv[i] != "--verbose":
            continue
        verbose_enabled = True
        break

    load_dotenv()
    prompt = sys.argv[1]
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    reply = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=prompt)

    print(reply.text)
    print(f"Prompt tokens: {reply.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {reply.usage_metadata.candidates_token_count}")
    

if __name__ == "__main__":
    main(sys.argv)


