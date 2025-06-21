import os

def write_file(working_directory, file_path, content):
    try:
        root = os.path.abspath(working_directory)
        path = os.path.join(root, file_path)
        if not os.path.abspath(path).startswith(root):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
        if not os.path.isfile(path):
            file_dir = os.path.dirname(path)
            if not os.path.isdir(file_dir):
                os.mkdir(file_dir)

        with open(path, "w") as f:
            f.write(content)

        return f'Successfully wrote to "{path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: {e}"      
        