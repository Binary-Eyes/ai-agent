import os
from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="writes content to the give file.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="the target path of the file to write. relative to the working directory",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="the content to write into the supplied file",
            ),
        },
    ),
)

def write_file(working_directory, file_path, content):
    try:
        abs_working_directory = os.path.abspath(working_directory)
        relative_path = os.path.join(working_directory, file_path)
        target_path = os.path.abspath(relative_path)
        if not target_path.startswith(abs_working_directory):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        target_directory = os.path.dirname(target_path)
        if not os.path.exists(target_directory):
            os.makedirs(target_directory)

        with open(target_path, "w") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"

    
