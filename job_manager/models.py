from django.db import models

class JobApplication(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('generated', 'AI Generated'),
        ('emailed', 'Emailed'),
    ]

    company_name = models.CharField(max_length=200)
    job_title = models.CharField(max_length=200)
    employer_email = models.EmailField(blank=True, null=True)
    
    # Input
    job_description_text = models.TextField(blank=True, help_text="Paste the job description here.")
    job_description_image = models.ImageField(upload_to='job_posts/', blank=True, null=True, help_text="Or upload a screenshot of the job post.")
    
    # Output
    generated_cv = models.TextField(blank=True, help_text="AI Generated CV matching the job description.")
    generated_cover_letter = models.TextField(blank=True, help_text="AI Generated Cover Letter.")
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.job_title} at {self.company_name}"
