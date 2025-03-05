# AI-Resume-Screener
This is an AI-powered Resume Screener that ranks resumes based on job descriptions using Natural Language Processing (NLP) techniques. The script extracts text from resumes, processes them using TF-IDF (Term Frequency-Inverse Document Frequency) and Cosine Similarity, and ranks candidates based on job relevance.

Features

✅ Automated Resume Ranking – Matches resumes to job descriptions and ranks them accordingly
✅ PDF Text Extraction – Uses pdfplumber to extract text from resumes
✅ NLP Processing – Uses sklearn for TF-IDF and similarity calculations
✅ Simple Setup – Just place resumes in a folder, add a job description, and run the script
✅ Efficient Processing – Can handle multiple resumes at once

Technologies Used

Programming Language: Python

Libraries: scikit-learn, pdfplumber, os

Development Tools: VS Code

Project Structure

📂 myproject/  
 ┣ 📂 Resumes/           # Folder containing all PDF resumes  
 ┣ 📄 jobDesc.txt        # Job description file  
 ┣ 📜 resume_parser.py   # Main script for ranking resumes 
 ┣ 📜 resume_matcher.py  # Script for checking similarities between resumes and job description 
 ┣ 📜 requirements.txt   # Required dependencies  

How to Run

1️⃣ Set Up Virtual Environment

Open terminal in VS Code (Ctrl + ~)

Navigate to your project folder:

cd "C:\Users\GEO\Documents\myproject"

Activate the virtual environment:

venv\Scripts\activate

Install required dependencies:

pip install -r requirements.txt

2️⃣ Add Resumes & Job Description

Place PDF resumes inside the Resumes/ folder.

Add job description in jobDesc.txt.

3️⃣ Run the Script

Execute the script:

python resume_screener.py

Expected Output

✅ jobDesc.txt found!
📂 Scanning Resumes Folder...
📄 Found 5 Resumes
✅ Extracted text from resume_1.pdf
✅ Extracted text from resume_2.pdf
...
🏆 Top 3 Relevant Resumes:
1️⃣ resume_3.pdf (0.29 match)
2️⃣ resume_1.pdf (0.28 match)
3️⃣ resume_5.pdf (0.23 match)

Future Enhancements

🚀 Improve keyword extraction with AI models
🚀 Add a web-based interface for better usability
🚀 Integrate with job application platforms

Author

📌 Emaan Bano – AI/ML Enthusiast | Computer Science Student📧 
Email: emaanbano.kc@gmail.com🔗 
LinkedIn: https://www.linkedin.com/in/emaan-bano-4b09a830b/📌 
GitHub: https://github.com/emaanb
