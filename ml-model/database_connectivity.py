from pymongo import MongoClient
from gridfs import GridFS
from bson.objectid import ObjectId
import os
from dotenv import load_dotenv
import langaugetranslation


# Connect to MongoDB
client = MongoClient('mongodb+srv://naeem:test111@alpha.rq2vnnk.mongodb.net/?retryWrites=true&w=majority&appName=alpha')  # Replace with your MongoDB connection string
db = client['mydatabase']  # Replace with your database name
collection = db['your_collection_name']  # Replace with your collection name
fs = GridFS(db, collection='fs')

admin_collection = db['Admins']


# Function to get file by ObjectId
def get_file_by_id(file_id):
    file = fs.get(ObjectId(file_id))
    return file

# Fetch the document only if docparsed is 0

document_with_condition = admin_collection.find_one({'docParsed': 0})  # Replace 'field_name_containing_id' with the actual field name containing the ObjectId, 'your_id_value' with the actual value, and 'docparsed' with the actual field name containing the docparsed flag

if document_with_condition:
    # Extract the ObjectId from the document
    file_id = document_with_condition['fileId']
    fileId = file_id

    # Get the file from GridFS using the ObjectId
    file = get_file_by_id(file_id)

    # Specify the output folder and file name
    opt_folder_path = os.path.join(os.getcwd(), "output")
    if not os.path.exists(opt_folder_path):
        os.makedirs(opt_folder_path)
    opt_file_name = "output.pdf"
    opt_file_path = os.path.join(opt_folder_path, opt_file_name)

    # Write the file data to the output file
    with open(opt_file_path, "wb") as opt_file:
        opt_file.write(file.read())

    # admin_collection.update_one(
    #     {'docParsed': 0},  # Filter to find the document to update
    #     {'$set': {'docParsed': 1}}  # Update the docParsed field to 1
    # )



    print(f"File successfully fetched from MongoDB to the path: {opt_folder_path}")
    print("Summarising the data \n")

else:
    print("No document found with docparsed=0")

