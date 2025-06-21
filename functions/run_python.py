import os

def run_python_file(working_directory, file_path):
    try:
        root = os.path.abspath(working_directory)
        path = os.path.join(root, file_path)
        if not os.path.abspath(path).startswith(root):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    except Exception as e:
        return f"Error: {e}"