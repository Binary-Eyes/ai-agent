import os

def get_files_info(working_directory, directory="."):
    abs_working_directory = os.path.abspath(working_directory)
    relative_directory = os.path.join(working_directory, directory)
    target_directory = os.path.abspath(relative_directory)
    if not target_directory.startswith(abs_working_directory):
        return f'  Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if os.path.isfile(target_directory):
        return f'  Error: "{directory}" is not a directory'

    result = ""
    content = os.listdir(target_directory)
    for entry in content:
        entry_path = os.path.join(target_directory, entry)
        result += f" - {entry}: file_size={os.path.getsize(entry_path)}, is_dir={os.path.isdir(entry_path)}\n"

    return result