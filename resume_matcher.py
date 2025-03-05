import os
import pdfplumber
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Paths
resumes_folder = "C:\\Users\\GEO\\Documents\\myproject\\Resumes"
job_desc_path = "C:\\Users\\GEO\\Documents\\myproject\\jobDesc.txt"

def extract_text_from_pdf(pdf_path):
    """Extract text from a given PDF file."""
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

# Read the job description
with open(job_desc_path, "r", encoding="utf-8") as file:
    job_description = file.read()

# Read all resumes and extract text
resume_texts = {}
for filename in os.listdir(resumes_folder):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(resumes_folder, filename)
        resume_texts[filename] = extract_text_from_pdf(pdf_path)

# TF-IDF Vectorization
vectorizer = TfidfVectorizer()
all_texts = [job_description] + list(resume_texts.values())
tfidf_matrix = vectorizer.fit_transform(all_texts)

# Compute Cosine Similarity
similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()

# Rank resumes by similarity
ranked_resumes = sorted(zip(resume_texts.keys(), similarities), key=lambda x: x[1], reverse=True)

# Print results
print("\n📊 Resume Ranking Based on Job Match:")
for rank, (resume, score) in enumerate(ranked_resumes, start=1):
    print(f"{rank}. {resume} - Similarity: {score:.2f}")

# Save results to a text file
results_path = os.path.join(resumes_folder, "resume_ranking.txt")
with open(results_path, "w", encoding="utf-8") as result_file:
    result_file.write("📊 Resume Ranking Based on Job Match:\n")
    for rank, (resume, score) in enumerate(ranked_resumes, start=1):
        result_file.write(f"{rank}. {resume} - Similarity: {score:.2f}\n")

print(f"\n✅ Results saved to: {results_path}")
