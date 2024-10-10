import os
import pytesseract
from PIL import Image
from pdf2image import convert_from_path
import summarisation_json
import googletrans
from pymongo import MongoClient
# from transformers import MBartForConditionalGeneration, MBartTokenizerFast


translator = googletrans.Translator()


client = MongoClient('mongodb+srv://naeem:test111@alpha.rq2vnnk.mongodb.net/?retryWrites=true&w=majority&appName=alpha')  # Replace with your MongoDB connection string
db = client['mydatabase']  # Replace with your database name
admin_collection = db['Admins']

# Paths and variables
poppler_path = r"C:\Program Files\poppler-23.11.0\Library\bin"
output_path = r"C:\Users\vinay\Downloads\output"
pdf_path = r"D:\vinayak\work\Python\pythonProject\output\output.pdf"
save_dir = r"C:\Users\vinay\Downloads\output"
text_to_match = ""

# def extract_text():
#
#
#     # english_text = english_text + " give me the json format of the data "
#
#     # summary = summarisation_json.summarised_data(english_text)
#     # text_to_match = summary
#     # print(f"Summary: {summary}\n")
#
#     filter_criteria = {'fileId': constants.fileId}
#     result = admin_collection.update_one(
#         filter_criteria,  # Filter to find the documents to update
#         {'$set': {'Summary': summary}}  # Update to create the Summary field and post the string text into it
#     )

# def translate_mbart(text, source_lang, target_lang):
#
#     # Load mBART model and tokenizer
#     model = MBartForConditionalGeneration.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")
#     tokenizer = MBartTokenizerFast.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")
#     tokenizer.src_lang = source_lang
#
#     # Split input text into chunks
#     chunk_size = 100# Adjust chunk size as needed
#     chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
#
#     # Generate translations for each chunk
#     translated_chunks = []
#     for chunk in chunks:
#         encoded_chunk = tokenizer(chunk, return_tensors="pt", truncation=True, padding=True)
#         generated_tokens = model.generate(**encoded_chunk, forced_bos_token_id=tokenizer.lang_code_to_id[target_lang])
#         translated_chunk = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
#         translated_chunks.extend(translated_chunk)  # Extend instead of append
#
#     # Concatenate translated chunks
#     translated_text = " ".join(translated_chunks)
#     return translated_text


def translate_marathi_english(text: str, dest='en') -> str:
    if not text:  # Handle empty text case
        return ""

    # Ensure UTF-8 encoding
    text = text.encode('utf-8').decode('utf-8')
    chunk_size = 100
    num_chunks = (len(text) + chunk_size - 1) // chunk_size
    translations = []
    # Translate each chunk and append the translations
    for i in range(num_chunks):
        chunk = text[i * chunk_size: (i + 1) * chunk_size]
        translation = translator.translate(chunk, dest=dest).text
        translations.append(translation)

    english_text = "".join(translations)

    # print("english_text : "+ english_text)
    return english_text




def convert_pdf(pdf_path = pdf_path , save_dir = output_path, res=500):
    images = convert_from_path(pdf_path, res, poppler_path=poppler_path, output_folder=save_dir)
    for i, image in enumerate(images):
        image.save(f"{output_path}/page_{i}.jpg", "JPEG")

    image_files = [os.path.join(output_path, f) for f in os.listdir(output_path)
                   if f.endswith(".jpg") or f.endswith(".png")]
    marathi_text_global = ""
    for image_file in image_files:
        try:
            # Use PIL to open the image and extract text using pytesseract
            with Image.open(image_file) as img:
                text = pytesseract.image_to_string(img, lang='mar')

            marathi_text_global += text

            print(f"Extracted text from image: {marathi_text_global}")

        except Exception as e:
            print(f"Error processing image {image_file}: {e}")

        # translate(marathi_text_global)

    # Use Chunker for efficient handling of potentially large text
    # english_text = translate_marathi_english(marathi_text_global, 'en')
    return marathi_text_global


