import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import PyPDF2

stop_words = set(stopwords.words('english'))

custom_stopwords = {
    "looking", "developer", "skilled", "required",
    "experience", "knowledge", "good", "must"
}

stop_words = stop_words.union(custom_stopwords)


def clean_text(text):
    text = text.lower()
    text = "".join([char for char in text if char not in string.punctuation])
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return " ".join(words)

def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text

# 👇 Put your resume PDF file name here
resume_path = "Shrushti_Resume.pdf"

resume_text = extract_text_from_pdf(resume_path)

job_description = """
Looking for a Python developer skilled in React, Machine Learning,
REST APIs, and database management.
"""

resume_clean = clean_text(resume_text)
jd_clean = clean_text(job_description)


vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform([resume_clean, jd_clean])

similarity_score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])

print("Match Percentage:", round(similarity_score[0][0] * 100, 2), "%")

# Get feature names
feature_names = vectorizer.get_feature_names_out()

# Convert vectors to array
resume_vector = tfidf_matrix[0].toarray()[0]
jd_vector = tfidf_matrix[1].toarray()[0]

missing_keywords = []

for i in range(len(feature_names)):
    if jd_vector[i] > 0 and resume_vector[i] == 0:
        missing_keywords.append(feature_names[i])

print("Match Percentage:", round(similarity_score[0][0] * 100, 2), "%")
print("Missing Keywords:", missing_keywords)

