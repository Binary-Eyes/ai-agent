from functions.get_files_info import get_files_info

def test_files_info(working_directory, relative_directory):
    directory_name = f"'{relative_directory}'"
    if (relative_directory == "."):
        directory_name = "current"
    
    print(f"Result for {directory_name} directory:")
    result = get_files_info(working_directory, relative_directory)
    print(f"{result}")

test_files_info("calculator", ".")
test_files_info("calculator", "pkg")
test_files_info("calculator", "/bin")
test_files_info("calculator", "../")