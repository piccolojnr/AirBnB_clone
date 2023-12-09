import re


def extract_method_info(method_string):
    """
    Extracts the class name, method name,
    and arguments from a method call string.

    Args:
        method_string (str): The method call string.

    Returns:
        list: A list containing the class name,
        method name, and parsed arguments.
    """
    # Define a regular expression pattern to match the method call structure
    pattern = r"^(\w*)?\.(\w+)\((.*)\)$"

    # Use re.match to check if the method_string matches the pattern
    match = re.match(pattern, method_string)
    if match:
        class_name, method_name, raw_arguments = match.groups()

        # Split arguments by commas and clean from leading/trailing spaces
        arguments_list = [
            arg.strip()
            .replace("'", "")
            .replace('"', "")
            .replace("{", "")
            .replace("}", "")
            for arg in raw_arguments.split(",")
        ]
        # Split each argument using colons
        arguments_list = [
            item.strip() for arg in arguments_list for item in arg.split(":")
        ]
        return [class_name, method_name] + arguments_list

    else:
        return None


# Example usage:
method_string1 = 'User.update("a5d10e79-08c5-4d90-9d19-df5d4d536e53", {"first_name": "John", "age": 89})'
result1 = extract_method_info(method_string1)

print(result1)
