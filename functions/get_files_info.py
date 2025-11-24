import os
from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
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

def get_files_info(working_directory, directory="."):
    abs_working_directory = os.path.abspath(working_directory)
    relative_directory = os.path.join(working_directory, directory)
    target_directory = os.path.abspath(relative_directory)
    if not target_directory.startswith(abs_working_directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if os.path.isfile(target_directory):
        return f'Error: "{directory}" is not a directory'

    result = ""
    content = os.listdir(target_directory)
    for entry in content:
        entry_path = os.path.join(target_directory, entry)
        result += f"- {entry}: file_size={os.path.getsize(entry_path)}, is_dir={os.path.isdir(entry_path)}\n"

    return result