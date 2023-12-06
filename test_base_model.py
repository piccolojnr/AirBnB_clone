import re


def extract_method_info(method_string):
    # Define a regular expression pattern to match the method call structure
    pattern = r"^(\w+)\.(\w+)\((.*)\)$"

    # Use re.match to check if the method_string matches the pattern
    match = re.match(pattern, method_string)
    if match:
        result = []
        result.append(match.groups()[0])
        result.append(match.groups()[1])
        result += [
            i.strip().replace(r"'", "").replace(r'"', "")
            for i in match.groups()[2].split(",")
        ]
        return result
    else:
        return None


method_string = (
    "User.count('name', 'John', 'age', 'ee9fa7fe-15de-4e69-   9d16-5513af783012')"
)
result = extract_method_info(method_string)

print(result)
