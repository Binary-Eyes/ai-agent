import os
import pathlib
import subprocess

def run_python_file(working_directory, file_path):
    try:
        root = os.path.abspath(working_directory)
        path = os.path.join(root, file_path)
        if not os.path.abspath(path).startswith(root):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(path):
            return f'Error: File "{file_path}" not found.'
        
        if not pathlib.Path(path).suffix == ".py":
            return f'Error: "{file_path}" is not a Python file.'
        
        completed = subprocess.run(
            args=["python3", path], 
            timeout=30,
            capture_output=True,
            text=True,
            cwd=os.path.dirname(path))
        
        output = ""
        if completed.returncode != 0:
            output += f"\nProcess exited with code {completed.returncode}"
        
        if len(completed.stdout) > 0:
            output += f"STDOUT:{completed.stdout}\n"

        if len(completed.stderr) > 0:
            output += f"STDERR:{completed.stderr}\n"

        if len(output) == 0:
            output = "No output produced"

        return output


    except Exception as e:
        return f"Error: executing Python file: {e}"