# Import necessary libraries
import os

# Check if the file exists
file_path = "jobDesc.txt"
if os.path.exists(file_path):
    print("✅ jobDesc.txt found!")

    # Read the job description
    with open(file_path, "r", encoding="utf-8") as file:
        job_description = file.read()

    print(f"🔹 File content length: {len(job_description)} characters")

    if job_description.strip():
        print("📄 Job Description Content:")
        print(job_description)
    else:
        print("⚠️ The file is empty!")
else:
    print("❌ jobDesc.txt not found!")
