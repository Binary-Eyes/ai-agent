import os

def get_files_info(working_directory, directory=None):
    try:
        path = os.path.abspath(directory)
        if not path.startswith(working_directory):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        if not os.path.isdir(directory):
            return f'Error: "{directory}" is not a directory'
    except Exception as e:
        return e


