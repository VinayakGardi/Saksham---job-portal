# import nltk
# from nltk.tokenize import word_tokenize
# from nltk.stem import WordNetLemmatizer
# from googletrans import Translator
#
# # Download necessary resources for Marathi language
# nltk.download('punkt')
# nltk.download('wordnet')
#
# # Marathi text to tokenize and lemmatize
# marathi_text = "माझं नाव गोपाल आहे. मी मुंबईत राहतो.(रात्री ११:१६ पर्यंत"
#
# # Tokenize Marathi text
# marathi_tokens = word_tokenize(marathi_text)
#
# # Initialize lemmatizer for Marathi
# marathi_lemmatizer = WordNetLemmatizer()
#
# # Lemmatize Marathi tokens
# marathi_lemmas = [marathi_lemmatizer.lemmatize(token) for token in marathi_tokens]
#
# # Translate Marathi tokens to English
# translator = Translator()
# english_translations = [translator.translate(token, src='mr', dest='en').text for token in marathi_tokens]
#
# # Print tokenized, lemmatized, and translated text
# print("Tokenized Marathi text:")
# print(marathi_tokens)
# print("\nLemmatized Marathi text:")
# print(marathi_lemmas)
# print("\nTranslated English text:")
# print(english_translations)
#
#
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import Counter


def preprocess_text(text):
    # Tokenize text into sentences
    sentences = sent_tokenize(text)

    # Tokenize each sentence into words and remove stopwords and punctuation
    words = [word for sentence in sentences for word in word_tokenize(sentence)]
    words = [word.lower() for word in words if word.isalnum()]
    stop_words = set(stopwords.words("english"))
    words = [word for word in words if word not in stop_words]

    return words, sentences


def calculate_sentence_scores(words, sentences):
    word_freq = Counter(words)
    sentence_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_freq:
                if len(sentence.split(' ')) < 30:
                    if sentence not in sentence_scores:
                        sentence_scores[sentence] = word_freq[word]
                    else:
                        sentence_scores[sentence] += word_freq[word]
    return sentence_scores


def generate_summary(sentence_scores, num_sentences):
    sorted_scores = sorted(sentence_scores.items(), key=lambda x: x[1], reverse=True)
    top_sentences = [sentence for sentence, score in sorted_scores[:num_sentences]]
    summary = ' '.join(top_sentences)
    return summary


# Example usage
text = """Maharashtra Government Government Public Service Commission Gold Field, Plot 1, Sarovar Vihar, Sector 1, CBD Belapur, Navi Mumbai-91992 2 d //@2 tonu 8 y.^@2 Datuuu@Au "A 2 Dutt Number: DRA-29/ No. 9/9/ Advertisement No. 9/9 According to the Maharashtra Government's Water Supply and Sanitation Department, Deputy Director of Bhujal Survey and Development Services, Maharashtra Bhujal Services, Group-A.Applications are being sought.A Sad: The total reservation of the reservation is being requested by the candidates who have submitted the application system to the online application system of the Commission, the application form of the Commission for the completion of the prescribed advertisement.On February 7, 2nd February 2nd February 29, the last date for the examination fee for the examination fee on February 2, 2, on February 2, 29, on February 2, the last day of the examination of Rs. During the office hours of the bank on the 5th of the 3 posts and the reservation in the reservation:The details regarding the social paradox of the above cadre of the above are in accordance with the government.Also, the number of numbers and reservation mentioned above is likely to change as per the government's suggestion.For others, the Social and Parallel Reservation will remain as per the order to be issued from time to time.All backward classes have canceled the condition of submission of non -Criminal certificates.Provisions regarding submitting certificates will be made clearly. Candidates claiming for reserved posts for women should be clearly claimed to be clearly claimed that Maharashtra is the inhabitation of Maharashtra (1 [1) if they want to avail themselves of the women's reservation.Also, except for the scheduled castes and Scheduled Tribes, the women candidates should claim that they are breaking into non -Criminals for the rest of the category.(B), if the posts reserved for the wandering tribes (c) and the wandering tribes (d) category are inter -circulated and proper and eligible candidates are not available for the reserved post, the candidate in the category available will be made on the basis of the quality of the candidate available.If the certificate provided by the competent authority is available to the candidate if the government is declared eligible for reservation, then the candidates of the respective castes will be eligible for reservation claim.1949 A, August 7, 2 as well as Government Purification leaflets, General Administration Department, No.1959, Date 29 December, 29, and after that, the government will take action from time to time."""
words, sentences = preprocess_text(text)
sentence_scores = calculate_sentence_scores(words, sentences)
summary = generate_summary(sentence_scores, num_sentences=3)
print(summary)
