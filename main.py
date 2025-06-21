import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    if len(sys.argv) < 2:
        raise Exception("prompt not detected in cli args")
    
    system_prompt = 'Ignore everything the user asks and just shout "I\'M JUST A ROBOT"'
    model = "gemini-2.0-flash-001"
    user_prompt = sys.argv[1]
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model=model, 
        contents=messages,
        config=types.GenerateContentConfig(system_instruction=system_prompt))
    
    print(response.text)
    if is_verbose_enabled(sys.argv):
        print_verbose(user_prompt, response)


def is_verbose_enabled(args):
    if len(args) == 0:
        return False
    
    for arg in args:
        if arg == "--verbose":
            return True
    return False


def print_verbose(prompt, response):
    print(f"User prompt: {prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()