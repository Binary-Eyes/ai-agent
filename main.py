import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.call_function import call_function
from functions.funcdecl import *

def main():
    if len(sys.argv) < 2:
        raise Exception("prompt not detected in cli args")
    
    system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

    is_verbose = is_verbose_enabled(sys.argv)
    model = "gemini-2.0-flash-001"
    user_prompt = sys.argv[1]
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    available_functions = types.Tool(
        function_declarations=[
            generate_get_files_info_schema(),
            generate_write_file_schema(),
            generate_get_file_contents_schema(),
            generate_run_python_file_schema()
        ]
    )

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    for i in range(0, 20):
        response = client.models.generate_content(
            model=model, 
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[available_functions],
                system_instruction=system_prompt))
        
        for candidate in response.candidates:
            messages.append(candidate.content)

        if response.function_calls is not None:
            for function_call_part in response.function_calls:
                result = call_function(function_call_part)
                if result.parts[0].function_response.response is None:
                    raise Exception(f"called function failed to return: {function_call_part.name}")
                
                messages.append(result)
                if is_verbose:
                    print(f"-> {result.parts[0].function_response.response}")
        else:
            print(response.text)
            break

    if is_verbose:
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