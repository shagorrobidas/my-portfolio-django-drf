from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction
import threading


class JobApplication(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('generated', 'AI Generated'),
        ('emailed', 'Emailed'),
    ]

    company_name = models.CharField(max_length=200, blank=True, default="Pending AI...")
    job_title = models.CharField(max_length=200, blank=True, default="Pending AI...")
    employer_email = models.EmailField(blank=True, null=True)
    
    # Input
    job_description_text = models.TextField(blank=True, help_text="Paste the job description here.")
    job_description_image = models.ImageField(upload_to='job_posts/', blank=True, null=True, help_text="Or upload a screenshot of the job post.")
    
    # Output text
    generated_cv = models.TextField(blank=True, help_text="AI Generated CV matching the job description.")
    generated_cover_letter = models.TextField(blank=True, help_text="AI Generated Cover Letter.")
    apply_email_subject = models.CharField(max_length=255, blank=True, help_text="AI Generated application email subject.")
    apply_email_body = models.TextField(blank=True, help_text="AI Generated application email body.")
    ai_analysis_report = models.TextField(blank=True, help_text="AI Strategic Analysis: how to crack this job, key skills, and strategy.")
    
    # Output Files
    cv_pdf = models.FileField(upload_to='generated_docs/cv/pdf/', blank=True, null=True)
    cv_word = models.FileField(upload_to='generated_docs/cv/word/', blank=True, null=True)
    cover_letter_pdf = models.FileField(upload_to='generated_docs/cover_letters/pdf/', blank=True, null=True)
    cover_letter_word = models.FileField(upload_to='generated_docs/cover_letters/word/', blank=True, null=True)
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.job_title} at {self.company_name}"



@receiver(post_save, sender=JobApplication)
def trigger_ai_generation(sender, instance, created, **kwargs):
    if instance.status == 'draft' and getattr(instance, '_skip_signal', False) is False:
        # Prevent recursion and multiple runs
        instance._skip_signal = True
        
        def run_task():
            from .ai_service import process_job_application_task
            process_job_application_task(instance.id)
            
        transaction.on_commit(lambda: threading.Thread(target=run_task).start())
