import os
from bson import ObjectId
from gridfs import GridFS
from pymongo import MongoClient

client = MongoClient('mongodb+srv://naeem:test111@alpha.rq2vnnk.mongodb.net/?retryWrites=true&w=majority&appName=alpha')
db = client['mydatabase']  # Replace with your database name
# collection = db['your_collection_name']  # Replace with your collection name
fs = GridFS(db, collection='fs')

admin_collection = db['Admins']
user_collection = db['Users']
data_show = ""


def get_file_by_id(file_id):
    file = fs.get(ObjectId(file_id))
    return file


# document_with_condition = admin_collection.find_one({'docParsed': 0})  # Replace 'field_name_containing_id' with the actual field name containing the ObjectId, 'your_id_value' with the actual value, and 'docparsed' with the actual field name containing the docparsed flag


# if document_with_condition:
#     # Extract the ObjectId from the document
#     file_id = document_with_condition['fileId']
#
#     # Get the file from GridFS using the ObjectId

def translate(fileId):
    file = get_file_by_id(fileId)

    # Specify the output folder and file name
    opt_folder_path = os.path.join(os.getcwd(), "output")
    if not os.path.exists(opt_folder_path):
        os.makedirs(opt_folder_path)
    opt_file_name = "mpsc.pdf"
    opt_file_path = os.path.join(opt_folder_path, opt_file_name)

    # Write the file data to the output file
    with open(opt_file_path, "wb") as opt_file:
        opt_file.write(file.read())




#     # admin_collection.update_one(
#     #     {'docParsed': 0},  # Filter to find the document to update
#     #     {'$set': {'docParsed': 1}}  # Update the docParsed field to 1
#     # )
#
#     print(f"File successfully fetched from MongoDB to the path: {opt_folder_path}")
#     print("Summarising the data ... \n")
#     marathi_text = langaugetranslation.convert_pdf()
#     print(marathi_text)
#     print("translating pdf to suitable language ...")
#     english_text = langaugetranslation.translate_marathi_english(marathi_text)
#     print(english_text)
#     print("extracting information ...")
#     data = summarisation_json.summarised_data(english_text)
#     data_show = data
#     print(data)
#
#     # store the summarised data
#     filter_criteria = {'fileId': file_id}
#     result = admin_collection.update_one(
#         filter_criteria,  # Filter to find the documents to update
#         {'$set': {'Summary': data}}  # Update to create the Summary field and post the string text into it
#     )
#     print("sucessfully stored extracted data in database")
# else:
#     print("No document found with docparsed=0")
#
# # call for matching algorithm
# Matching_keywords.match_data(data_show)
