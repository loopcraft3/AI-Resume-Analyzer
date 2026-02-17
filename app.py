

import streamlit as st

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="centered"
)
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

def extract_text_from_pdf(uploaded_file):
    text = ""
    reader = PyPDF2.PdfReader(uploaded_file)
    for page in reader.pages:
        text += page.extract_text()
    return text

st.markdown("<h1 style='text-align: center;'>📄 AI Resume–Job Match Analyzer</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: grey;'>Compare your resume with job descriptions instantly</p>", unsafe_allow_html=True)
st.markdown("---")


col1, col2 = st.columns(2)

with col1:
    uploaded_resume = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

with col2:
    job_description = st.text_area("Paste Job Description", height=200)


if st.button("Analyze"):
    if uploaded_resume and job_description:
        with st.spinner("Analyzing resume... ⏳"):

            resume_text = extract_text_from_pdf(uploaded_resume)

            resume_clean = clean_text(resume_text)
            jd_clean = clean_text(job_description)

            # Extract important words from JD automatically
            jd_words = set(jd_clean.split())

            resume_words = set(resume_clean.split())

            # Keep only words that appear in JD
            resume_filtered = " ".join([word for word in resume_words if word in jd_words])
            jd_filtered = " ".join(jd_words)

            vectorizer = TfidfVectorizer()
            tfidf_matrix = vectorizer.fit_transform([resume_filtered, jd_filtered])


            similarity_score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])

            match_percent = round(similarity_score[0][0] * 100, 2)

            st.markdown("---")
            st.subheader("📊 Analysis Result")

            st.subheader("Match Percentage")
            st.progress(int(match_percent))

            if match_percent < 40:
                st.markdown(f"<h3 style='color:red;'>Match Score: {match_percent}%</h3>", unsafe_allow_html=True)
                st.error("Low Match ❌ – Resume needs improvement.")
            elif match_percent < 70:
                st.markdown(f"<h3 style='color:orange;'>Match Score: {match_percent}%</h3>", unsafe_allow_html=True)
                st.warning("Moderate Match ⚠️ – You meet many requirements.")
            else:
                st.markdown(f"<h3 style='color:green;'>Match Score: {match_percent}%</h3>", unsafe_allow_html=True)
                st.success("Strong Match ✅ – Resume is highly aligned!")


            feature_names = vectorizer.get_feature_names_out()
            resume_vector = tfidf_matrix[0].toarray()[0]
            jd_vector = tfidf_matrix[1].toarray()[0]

            missing_skills = []

            for i in range(len(feature_names)):
                if jd_vector[i] > 0 and resume_vector[i] == 0:
                    missing_skills.append(feature_names[i])

            if missing_skills:
                st.subheader("Missing Skills")
                st.write(", ".join(missing_skills))
            else:
                st.success("Great! No major skills missing 🎉")

    else:
        st.warning("Please upload resume and paste job description.")
