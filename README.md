📄 AI Resume–Job Match Analyzer
An AI-powered resume screening web application that compares resumes with job descriptions using Natural Language Processing (NLP). The system calculates a match percentage and identifies missing skills to help candidates improve job alignment.


🌐 Live App: https://your-app-name.streamlit.app](https://ai-resume-analyzer-hzmv7uajt8xq6phpzsw8ue.streamlit.app/
💻 GitHub Repository: https://github.com/loopcraft3/AI-Resume-Analyzer


Project Overview
This project simulates an ATS (Applicant Tracking System)-style resume screening tool. It analyzes the similarity between a candidate’s resume and a job description using NLP techniques such as TF-IDF vectorization and cosine similarity.
The goal is to provide:

A realistic match percentage
Skill gap detection
A simple and interactive interface for real-time analysis

✨ Features

📄 Upload Resume (PDF format)
📝 Paste Job Description
📊 Match Percentage Calculation
📌 Automatic Keyword Extraction from Job Description
❗ Missing Skills Identification
🎨 Interactive and clean Streamlit UI
⚡ Real-time analysis

🛠 Tech Stack
Python
scikit-learn
Natural Language Processing (NLP)
TF-IDF Vectorization
Cosine Similarity
Streamlit
PyPDF2
Git & GitHub

⚙️ How It Works

Extracts text from the uploaded resume (PDF).
Cleans and preprocesses text:
Lowercasing
Stopword removal
Punctuation removal
Dynamically extracts relevant keywords from the job description.
Converts resume and JD text into numerical vectors using TF-IDF.
Computes similarity score using cosine similarity.

Displays:
Match Percentage
Match Category (Low / Moderate / Strong)
Missing Skills

📦 Installation (Run Locally)
1️⃣ Clone the Repository
git clone https://github.com/loopcraft3/Ai-Resume-Analyzer.git
cd Ai-Resume-Analyzer

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run the Application
streamlit run app.py

🎯 Use Case

This tool can help:
Students preparing for placements
Job applicants tailoring resumes
Understanding ATS-style resume filtering
Practicing NLP-based text similarity techniques

📌 Future Improvements

Smarter skill extraction using NLP techniques
Synonym matching
Score breakdown by skill category
PDF report download
Improved UI styling

👩‍💻 Author

Shrushti Waghmare
B.E. Information Technology
Passionate about AI, Machine Learning, and Full-Stack Development

🔥 This README looks professional and recruiter-ready.

If you want, I can also give:
