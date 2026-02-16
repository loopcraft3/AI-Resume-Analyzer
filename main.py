import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = text.lower()
    text = "".join([char for char in text if char not in string.punctuation])
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return " ".join(words)

# Sample texts
resume = "Python developer with experience in React and Machine Learning"
job_description = "Looking for a Machine Learning developer skilled in Python"

resume_clean = clean_text(resume)
jd_clean = clean_text(job_description)

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform([resume_clean, jd_clean])

similarity_score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])

print("Match Percentage:", round(similarity_score[0][0] * 100, 2), "%")
