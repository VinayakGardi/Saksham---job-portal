import json
import google.generativeai as genai

genai.configure(api_key="AIzaSyAAqu1su3VNZ2fEJM0UiR_OhU9a0LA53KY")


def summarised_data(input_text):
    generation_config = {
        "temperature": 0.5,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 2048,
    }

    safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
    ]

    model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                  generation_config=generation_config,
                                  safety_settings=safety_settings)

    prompt_parts = [
        input_text + """extract these fields in json format job title, organisation ,website ,education ,selection process, number of position, application start date, application end date, fees, payment method, category, required documents , min age, max age, disclaimer """,

    ]
    response = model.generate_content(prompt_parts)
    return clean_json_string(response.text)


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
