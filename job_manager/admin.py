# Custom Unfold Admin for Job Applications
import os
from django.contrib import admin
from django.core.mail import EmailMessage
from django.contrib import messages
from unfold.admin import ModelAdmin
from unfold.decorators import action

from .models import JobApplication
from .ai_service import generate_application_documents

@admin.register(JobApplication)
class JobApplicationAdmin(ModelAdmin):
    list_display = ('job_title', 'company_name', 'employer_email', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('job_title', 'company_name', 'employer_email')
    readonly_fields = (
        'generated_cv', 'generated_cover_letter', 'apply_email_subject', 
        'apply_email_body', 'ai_analysis_report', 'status', 
        'cv_pdf', 'cv_word', 'cover_letter_pdf', 'cover_letter_word'
    )
    
    fieldsets = (
        ("Job Details", {
            'fields': ('company_name', 'job_title', 'employer_email', 'status')
        }),
        ("Job Posting Input", {
            'fields': ('job_description_text', 'job_description_image')
        }),
        ("AI Strategic Analysis & Interview Coach", {
            'fields': ('ai_analysis_report',)
        }),
        ("AI Outreach Email ('HR Crack' version)", {
            'fields': ('apply_email_subject', 'apply_email_body')
        }),
        ("AI Generated Documents", {
            'fields': ('generated_cv', 'generated_cover_letter')
        }),
        ("Downloads", {
            'fields': ('cv_pdf', 'cv_word', 'cover_letter_pdf', 'cover_letter_word')
        }),
    )
    
    actions = ['send_application_email']

    @action(description="Send Application Email")
    def send_application_email(self, request, queryset):
        sent_count = 0
        for application in queryset:
            if application.status != 'generated':
                messages.warning(request, f"Skipped {application.company_name}: Status must be 'AI Generated'.")
                continue
                
            if not application.employer_email:
                messages.error(request, f"Cannot send email for {application.company_name}: No employer email provided.")
                continue
                
            try:
                subject = application.apply_email_subject or f"Application for {application.job_title}"
                body = application.apply_email_body or application.generated_cover_letter
                
                email = EmailMessage(
                    subject=subject,
                    body=body,
                    to=[application.employer_email],
                )
                
                # Attach CV
                if application.cv_pdf and os.path.exists(application.cv_pdf.path):
                    email.attach_file(application.cv_pdf.path)
                else:
                    email.attach(f"My_CV_{application.company_name.replace(' ', '_')}.txt", application.generated_cv, "text/plain")
                
                # Attach Cover Letter
                if application.cover_letter_pdf and os.path.exists(application.cover_letter_pdf.path):
                    email.attach_file(application.cover_letter_pdf.path)
                
                email.send(fail_silently=False)
                
                application.status = 'emailed'
                application.save(update_fields=['status'])
                sent_count += 1
            except Exception as e:
                messages.error(request, f"Failed to send email to {application.employer_email}: {str(e)}")
                
        if sent_count > 0:
            messages.success(request, f"Successfully sent {sent_count} application email(s)!")
