import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from job_manager.ai_service import generate_application_documents
from job_manager.models import JobApplication

job_text = """
Hiring Backend (Python) Developer for Ayisha Soft
We are looking for a backend developer with strong hands-on experience in third-party API integration.
Experience with CRM, ATS, or candidate platforms is not mandatory, but it will be a bonus point.

Key Requirements
1. Experience integrating third-party APIs
2. Strong experience with system optimization and performance improvement
3. Working experience with PostgreSQL
4. Experience with message brokers such as Redis or RabbitMQ
5. Working experience with asynchronous programming
6. Strong problem-solving skills
7. Ability to understand requirements and implement reliable backend solutions.

Job Details
Workplace: Remote initially, later in-office.
Weekend: Friday and Saturday, 2 days
Salary Range: BDT 35,000-45,000
Send your updated CV/Resume to career@ayishasoft.com
"""

print("Running AI Generation via OpenAI (GPT-4o)...")
cv, cl = generate_application_documents(job_description_text=job_text)

print("\n\n================ COVER LETTER ================\n")
print(cl)
print("\n\n===================== CV =====================\n")
print(cv)

# Optional: Save to DB to show in admin
app = JobApplication.objects.create(
    company_name="Ayisha Soft",
    job_title="Backend (Python) Developer",
    employer_email="career@ayishasoft.com",
    job_description_text=job_text,
    generated_cv=cv,
    generated_cover_letter=cl,
    status='generated'
)
print(f"\nSaved Application ID: {app.id}")
