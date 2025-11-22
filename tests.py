from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.write_file import write_file

def test_files_info(working_directory, relative_directory):
    directory_name = f"'{relative_directory}'"
    if (relative_directory == "."):
        directory_name = "current"
    
    print(f"Result for {directory_name} directory:")
    result = get_files_info(working_directory, relative_directory)
    print(f"{result}")

# test_files_info("calculator", ".")
# test_files_info("calculator", "pkg")
# test_files_info("calculator", "/bin")
# test_files_info("calculator", "../")

# print(get_file_content("calculator", "lorem.txt"))
# print(get_file_content("calculator", "main.py"))
# print(get_file_content("calculator", "pkg/calculator.py"))
# print(get_file_content("calculator", "/bin/cat"))
# print(get_file_content("calculator", "pkg/does_not_exist.py"))

print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))