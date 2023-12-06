import re


def extract_method_info(method_string):
    """
    Extracts the class name, method name, and arguments from a method call string.

    Args:
        method_string (str): The method call string.

    Returns:
        list: A list containing the class name, method name, and parsed arguments.
    """
    # Define a regular expression pattern to match the method call structure
    pattern = r"^(\w*)?\.(\w+)\((.*)\)$"

    # Use re.match to check if the method_string matches the pattern
    match = re.match(pattern, method_string)
    if match:
        class_name, method_name, raw_arguments = match.groups()

        # Split arguments by commas and clean from leading/trailing spaces
        arguments_list = [
            arg.strip().replace("'", "").replace('"', "")
            for arg in raw_arguments.split(",")
        ]

        return [class_name, method_name] + arguments_list

    else:
        return None


# Example usage:
method_string1 = (
    'User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", "first_name", 42, 3.14)'
)
result1 = extract_method_info(method_string1)

method_string2 = ".destroy()"
result2 = extract_method_info(method_string2)

if result1:
    print(f"Class Name: {result1[0]}")
    print(f"Method Name: {result1[1]}")
    print(f"Parsed Arguments: {result1[2:]}")
    print(result1)
else:
    print("Invalid method call string.")

if result2:
    print(f"Class Name: {result2[0]}")
    print(f"Method Name: {result2[1]}")
    print(f"Parsed Arguments: {result2[2:]}")
    print(result2)
else:
    print("Invalid method call string.")
