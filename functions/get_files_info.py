import os

def get_files_info(working_directory, directory=None):
    try:
        root = os.path.abspath(working_directory)
        path = os.path.join(root, directory)
        if not os.path.abspath(path).startswith(root):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(path):
            return f'Error: "{directory}" is not a directory'
        
        items = []
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            is_dir = False
            
            if os.path.isdir(item_path):
                is_dir = True

            size = os.path.getsize(item_path)
            items.append(f"- {item}: file_size={size} bytes, is_dir={is_dir}")

        return "\n".join(items)

    except Exception as e:
        return f"Error: {e}"


