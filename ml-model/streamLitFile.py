import json

import streamlit as st
import os
import langaugetranslation  # Assuming this is your module containing the PDF extraction and translation functions
from summarisation_json import summarised_data  # Assuming this is your function for summarizing data


def main():
    # Set page title
    st.set_page_config(page_title="Data Summarization")

    # Title and instructions
    st.title("Data Summarization")
    st.write("This app reads a local PDF file uploaded by the user, performs summarization, and displays the results.")

    # File upload section
    uploaded_file = st.file_uploader("Upload PDF file", type=['pdf'])

    # Button to trigger summarization
    if uploaded_file is not None:
        # Save the uploaded file to output folder with name "output.pdf"
        output_folder = "output"
        os.makedirs(output_folder, exist_ok=True)
        output_file_path = os.path.join(output_folder, "output.pdf")
        with open(output_file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Perform summarization
        st.write("Translating and extracting text from the file....")
        marathi_text = langaugetranslation.convert_pdf(output_file_path)
        english_text = langaugetranslation.translate_marathi_english(marathi_text)
        data = summarised_data(english_text)

        # Display summarization result
        st.write("Summarised Data:")
        st.write(data)
        data = json.loads(data)


        st.title("The job details from the given document are ")
        # Display each key-value pair with appropriate styling
        for key, value in data.items():
            if value is not None:
                st.write(f"**{key.capitalize()}:** {value}")
            else:
                st.write(f"**{key.capitalize()}:** Not specified")


if __name__ == "__main__":
    main()
