import os

MAX_CHAR = 10000

def get_file_content(working_directory, file_path):
    try:
        root = os.path.abspath(working_directory)
        path = os.path.join(root, file_path)
        if not os.path.abspath(path).startswith(root):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        with open(path, "r") as f:
            contents = f.read(MAX_CHAR)
            if len(contents) == MAX_CHAR:
                contents += f'[...File "{file_path}" truncated at 10000 characters]'
            
            return contents
        
    except Exception as e:
        return f"Error: {e}"
    
