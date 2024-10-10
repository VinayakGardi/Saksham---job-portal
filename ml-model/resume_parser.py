import PyPDF2
def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as f:
        pdf_reader = PyPDF2.PdfReader(f)
        num_pages = len(pdf_reader.pages)

        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

    return text

# Example usage
pdf_file_path = r"D:\vinayak\work\resume\my_resume_17_02_24.pdf"
extracted_text = extract_text_from_pdf(pdf_file_path)
print(extracted_text+"\n")
