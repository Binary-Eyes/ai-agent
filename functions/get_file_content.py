import os

MAX_CHARS = 10000

def get_file_content(working_directory, file_path):
    try:
        abs_working_directory = os.path.abspath(working_directory)
        relative_path = os.path.join(working_directory, file_path)
        target_path = os.path.abspath(relative_path)
        if not target_path.startswith(abs_working_directory):
            return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'

        if os.path.isdir(target_path):
            return f'Error: "{file_path}" is not a file'
        
        with open(target_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            next = f.read(1)
            if next is not None:
                file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            return file_content_string
    except Exception as e:
        return f"Error: {e}"