import pdfplumber
import os

# Path to the folder containing resumes
resumes_folder = "C:\\Users\\GEO\\Documents\\myproject\\Resumes"

def extract_text_from_pdf(pdf_path):
    """Extract text from a given PDF file."""
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

# Process all PDFs in the Resumes folder
if os.path.exists(resumes_folder):
    for filename in os.listdir(resumes_folder):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(resumes_folder, filename)
            print(f"📄 Processing: {filename}")
            
            resume_text = extract_text_from_pdf(pdf_path)
            
            # Save extracted text in a new text file
            text_file_path = os.path.join(resumes_folder, f"{filename}.txt")
            with open(text_file_path, "w", encoding="utf-8") as text_file:
                text_file.write(resume_text)
            
            print(f"✅ Extracted text saved: {text_file_path}\n")
else:
    print("❌ Resumes folder not found!")

