## Application Preview

### Home Screen
![Home](home.png)

### Analysis Output
![Output](output.png)
# AI Resume Analyzer (LLM Powered)

An AI-powered web application that analyzes resumes against job descriptions and provides ATS-style feedback using a Large Language Model.

## Features
- Upload Resume (PDF)
- Paste Job Description
- ATS Match Score
- Strengths Identification
- Missing Skills Detection
- Improvement Suggestions

## Tech Stack
- Python
- Streamlit
- OpenRouter (Mistral-7B LLM)
- PyPDF2

## How to Run

1. Clone the repository
2. Install dependencies:
   pip install -r requirements.txt

3. Add your API key in:
   .streamlit/secrets.toml

4. Run the application:
   streamlit run app.py

## Use Case
Helps job seekers optimize their resumes for specific roles using AI-based analysis.
