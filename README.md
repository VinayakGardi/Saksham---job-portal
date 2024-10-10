
#  Saksham - Job Portals for governnment professions                           



## Overview
This project aims to build a job recommendation system that helps candidates find government job opportunities based on their qualifications. The system automates the process of extracting job details from official government documents, translating them into English, and matching them with candidate profiles to suggest the most suitable jobs. The entire process leverages Optical Character Recognition (OCR), language translation, text processing, and database integration for efficient recruitment.
## Features
#### PDF to Image Conversion

- Converts uploaded PDF job documents into individual image files for each page using pdf2image.Supports multi-page PDF documents by generating a separate image file for each page.Ensures that even complex PDF structures are accurately represented in the image format for subsequent processing.

#### Image to Text Extraction (Regional Language)
- Extracts text from the converted image files using pytesseract, a powerful OCR library.Retains the text in its original regional language format (e.g., Marathi, Hindi) for further processing. Generates individual text files corresponding to each image for data persistence and future reference.

#### Regional Language to English Translation
- Translates the extracted text from the regional language to English using the googletrans library. Supports multiple regional languages and ensures accurate language detection and translation. Handles complex sentences, keywords, and terminologies specific to the job domain.Data Cleaning and Preprocessing


#### Text Data Conversion to JSON Format
- Extracts key information such as job title, qualifications, responsibilities, eligibility criteria, and application details.Converts the structured information into a standardized JSON format for efficient data storage and retrieval.Enables easy integration with databases (MongoDB) and compatibility with other data processing modules.

#### Candidate Profile Matching
- Compares the extracted job data with candidate profiles stored in a MongoDB database.Utilizes Machine Learning algorithms to find the most relevant jobs for each candidate based on their qualifications, skills, and experience.Calculates a similarity score to rank job recommendations.

#### Job Suggestion and Recommendation
- Suggests suitable government job opportunities to candidates based on the similarity scores.Provides personalized job notifications and recommendations, enhancing the overall user experience. Continuously updates the job suggestions as new job postings or candidate profiles are added.



## Technology Stack 

- Programming Language: Python
- Libraries: pytesseract, pdf2image, googletrans, spacy, pymongo, gridfs, PyPDF2, PIL
- Database: MongoDB (for storing candidate profiles and job data)
- Machine Learning: NLP techniques and ML models for text processing and matching.
## Usage
- Upload a government job PDF document to the system.
- The system will automatically convert the PDF to images and extract text in the regional language.
- Translated text is cleaned and converted to JSON format.
- The system will match the job details with candidate profiles in the database.
- Candidates receive job suggestions based on their profile.

## ScreenShots
