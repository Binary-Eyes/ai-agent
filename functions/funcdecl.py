from google.genai import types

def generate_write_file_schema():
    return types.FunctionDeclaration(
        name="write_file",
        description="Overrides an existing file or writes a new one, constrainted to files within the working directory",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "file_path": types.Schema(
                    type=types.Type.STRING,
                    description="The file to write to, relative to the working directory. If not provided, raise exception.",
                ),
                "content": types.Schema(
                    type=types.Type.STRING,
                    description="The text contents to write into the file",
                ),
            },
        ),
    )


def generate_run_python_file_schema():
    return types.FunctionDeclaration(
        name="run_python_file",
        description="Executes the given python file, constrained to the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "file_path": types.Schema(
                    type=types.Type.STRING,
                    description="The python file to run, relative to the working directory. If not provided, raise exception.",
                ),
            },
        ),
    )


def generate_get_file_contents_schema():
    return types.FunctionDeclaration(
        name="get_file_content",
        description="Reads and returns the content of a given file based on its path, constrained to the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "file_path": types.Schema(
                    type=types.Type.STRING,
                    description="The file to read, relative to the working directory. If not provided, raise exception.",
                ),
            },
        ),
    )


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