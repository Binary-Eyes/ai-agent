from google import genai
from google.genai import types

def generate_save_file_schema():
    pass

def generate_run_python_file_schema():
    pass

def generate_get_file_contents_schema():
    pass

def generate_get_files_info_schema():
    return types.FunctionDeclaration(
        name="get_files_info",
        description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "directory": types.Schema(
                    type=types.Type.STRING,
                    description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
                ),
            },
        ),
    )