import os
import pathlib
import subprocess

def run_python_file(working_directory, file_path):
    try:
        root = os.path.abspath(working_directory)
        path = os.path.join(root, file_path)
        if not os.path.abspath(path).startswith(root):
            return f'Error: Cannot read "{path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(path):
            return f'Error: File "{path}" not found.'
        
        if not pathlib.Path(path).suffix == ".py":
            return f'Error: "{path}" is not a Python file.'
        
        completed = subprocess.run(
            args=["python3", path], 
            timeout=30,
            working_directory=root,
            capture_output=True,
            text=True,
            cwd=os.path.dirname(path))
        
        output = ""
        if len(completed.stdout) > 0:
            output += f"STDOUT: {completed.stdout}"

        if len(output) == 0:
            output = "No output produced"

        return output


    except Exception as e:
        return f"Error: executing Python file: {e}"