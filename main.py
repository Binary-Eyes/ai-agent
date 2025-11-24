import os
import sys
from google import genai
from google.genai import types
from google.genai import Client
from dotenv import load_dotenv
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.run_python_file import schema_run_python_file
from functions.write_file import schema_write_file

def check_verbose_requested(args):
    for i in range(2, len(args)):
        if sys.argv[i] == "--verbose":
            return True
    return False


def print_verbose_output(prompt, reply):
    print(f"User prompt: {prompt}")
    print(f"Prompt tokens: {reply.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {reply.usage_metadata.candidates_token_count}")


def main(args):
    if len(args) < 2:
        print("WARNING: no prompt supplied to agent")
        sys.exit(1)

    available_functions = types.Tool(
        function_declarations=[
            schema_get_file_content,
            schema_get_files_info,
            schema_run_python_file,
            schema_write_file,
        ]
    )

    load_dotenv()
    is_verbose = check_verbose_requested(args)
    system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

    prompt = sys.argv[1]
    api_key = os.environ.get("GEMINI_API_KEY")
    client = Client(api_key=api_key)
    reply = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=prompt,        
        config=types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=system_prompt))

    if reply.function_calls is not None:
        for function_call_part in reply.function_calls:
            print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(reply.text)

    if is_verbose:
        print_verbose_output(prompt, reply)


if __name__ == "__main__":
    main(sys.argv)


