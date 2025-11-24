import os
import subprocess
from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes the given python file.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="the target path of the file to execute. relative to the working directory",
            ),
                "args": types.Schema(
                type=types.Type.ARRAY,
                description="added arguments supplied to the execution of the file",
                items=types.Schema(type=types.Type.STRING),
            ),
        },
    ),
)


def run_python_file(working_directory, file_path, args=[]):
    try:
        abs_working_directory = os.path.abspath(working_directory)
        relative_path = os.path.join(working_directory, file_path)
        target_path = os.path.abspath(relative_path)
        if not target_path.startswith(abs_working_directory):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.exists(target_path):
            return f'Error: File "{file_path}" not found.'
        
        if not target_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'
        
        cmd = ["python", target_path] + args
        result = subprocess.run(cmd, cwd=abs_working_directory, timeout=30, capture_output=True, text=True)
        result_string = ""
        if len(result.stdout) > 0:        
            result_string += f"STDOUT:{result.stdout}\n"

        if len(result.stderr) > 0:
            result_string += f"STDERR:{result.stderr}\n"

        if result.returncode != 0:
            result_string += f"Process exited with code {result.returncode}\n"
        
        if len(result_string) > 0:
            return result_string
        else:
            return "No output produced."
    except Exception as e:
        return f"Error: executing Python file: {e}"