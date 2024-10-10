import json
import re
def clean_json_string(json_string):
    # Initialize counters and flag variables
    curly_brace_count = 0
    start_index = None
    end_index = None
    in_string = False

    # Iterate over characters in the input string
    for i, char in enumerate(json_string):
        # Handle string literals
        if char == '"':
            in_string = not in_string
        # Track opening and closing curly braces
        elif char == '{' and not in_string:
            if curly_brace_count == 0:
                start_index = i
            curly_brace_count += 1
        elif char == '}' and not in_string:
            curly_brace_count -= 1
            if curly_brace_count == 0:
                end_index = i + 1
                break

    # Extract the JSON object if found
    if start_index is not None and end_index is not None:
        return json_string[start_index:end_index]
    else:
        return ""


dirty_string = 'Some text before {"key": "value"} and some text after'
cleaned_json = clean_json_string(dirty_string)
print(cleaned_json)  # Output: {"key": "value"}