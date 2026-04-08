from functions.get_file_content import get_file_content

def test():
    # Test truncation
    result = get_file_content("calculator", "lorem.txt")
    # Check that it's truncated properly...
    if len(result) > 10000 and result.endswith("10000 characters]"):
        print("truncated")

    # Test other cases
    result = get_file_content("calculator", "main.py")
    print(result)

    result = get_file_content("calculator", "pkg/calculator.py")
    print(result)

    result = get_file_content("calculator", "/bin/cat")
    print(result)

    result = get_file_content("calculator", "pkg/does_not_exist.py")
    print(result)

if __name__ == "__main__":
    test()
