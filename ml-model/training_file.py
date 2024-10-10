import pandas as pd
from faker import Faker  # For generating fake numeric data

# Initialize Faker to generate fake numeric data
fake = Faker()

# Function to generate Marathi sentences and English translations
def generate_data(num_samples):
    marathi_sentences = []
    english_translations = []
    for _ in range(num_samples):
        # Generate Marathi sentence (dummy data)
        marathi_sentence = fake.sentence(nb_words=10, variable_nb_words=True, ext_word_list=None)
        marathi_sentences.append(marathi_sentence)

        # Translate Marathi sentence to English (dummy translation)
        english_translation = fake.sentence(nb_words=10, variable_nb_words=True, ext_word_list=None)
        english_translations.append(english_translation)
    return marathi_sentences, english_translations

# Function to generate fake numeric data
def generate_numeric_data(num_samples):
    numeric_data = []
    for _ in range(num_samples):
        # Generate fake numeric data (dummy data)
        numeric_value = fake.random_number(digits=4)
        numeric_data.append(numeric_value)
    return numeric_data

# Generate Marathi sentences, English translations, and numeric data
num_samples = 100  # Number of samples to generate
marathi_sentences, english_translations = generate_data(num_samples)
numeric_data = generate_numeric_data(num_samples)

# Create a DataFrame
data = {
    'Marathi Sentence': marathi_sentences,
    'English Translation': english_translations,
    'Numeric Data': numeric_data
}
df = pd.DataFrame(data)

# Write DataFrame to CSV file
csv_file = "marathi_english_numeric_data.csv"
df.to_csv(csv_file, index=False)

print(f"CSV file '{csv_file}' generated successfully with {num_samples} samples.")
