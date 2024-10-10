import spacy
from pymongo import MongoClient

# Load the language model
nlp = spacy.load("en_core_web_lg")

client = MongoClient('mongodb+srv://naeem:test111@alpha.rq2vnnk.mongodb.net/?retryWrites=true&w=majority&appName=alpha')  # Replace with your MongoDB connection string
db = client['mydatabase']  # Replace with your database name
user_collection = db['Users']
admin_collection = db['Admins']


def match_data(data):
    num_entries = user_collection.count_documents({})

    for document in user_collection.find():
        document_location = document['location']
        document_experience = document['experience']
        document_education = document['education']
        document_age = document['age']
        document_category = document['category']

        # print("category : "+ document_category+"\n\n")


        document_user = document_category

        similarity = find_ratio(document_user , data)

        if(similarity > 0.3):
            document_summary = admin_collection.find_one({'Summary': data})
            admin_id = document_summary['_id']
            user_collection.update_one({'_id': document['_id']}, {'$set': {'eligible_jobs': admin_id}})


def find_ratio(document_user , document_jd )  :

    # Process the sentences with spaCy
    job_desc = nlp(document_jd)
    user_data = nlp(document_user)
    num_entries = user_collection.count_documents({})
    # Compute similarity between the two sentences
    similarity = user_data.similarity(job_desc)

    print(f"Similarities  : {similarity}\n")
    return similarity

