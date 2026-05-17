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
    readonly_fields = ('generated_cv', 'generated_cover_letter', 'status')
    
    actions = ['send_application_email']

    def save_model(self, request, obj, form, change):
        is_new = obj.pk is None
        # Save first to get the image path if uploaded
        super().save_model(request, obj, form, change)
        
        if obj.status == 'draft':
            try:
                image_path = obj.job_description_image.path if obj.job_description_image else None
                
                # Check if we have API KEY
                from django.conf import settings
                if not settings.OPENAI_API_KEY:
                    messages.error(request, "OPENAI_API_KEY is not set in environment or settings. Generation skipped.")
                    return
                
                cv, cover_letter = generate_application_documents(
                    job_description_text=obj.job_description_text,
                    job_image_path=image_path
                )
                
                obj.generated_cv = cv
                obj.generated_cover_letter = cover_letter
                
                if "Error generating documents" not in cover_letter:
                    obj.status = 'generated'
                    messages.success(request, "AI CV and Cover Letter generated successfully!")
                else:
                    messages.error(request, cover_letter)
                    
                obj.save(update_fields=['generated_cv', 'generated_cover_letter', 'status'])
            except Exception as e:
                messages.error(request, f"Generation failed: {str(e)}")

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
                email = EmailMessage(
                    subject=f"Application for {application.job_title}",
                    body=application.generated_cover_letter,
                    to=[application.employer_email],
                )
                # Attach the CV as a text file
                email.attach(f"My_CV_{application.company_name.replace(' ', '_')}.txt", application.generated_cv, "text/plain")
                email.send(fail_silently=False)
                
                application.status = 'emailed'
                application.save(update_fields=['status'])
                sent_count += 1
            except Exception as e:
                messages.error(request, f"Failed to send email to {application.employer_email}: {str(e)}")
                
        if sent_count > 0:
            messages.success(request, f"Successfully sent {sent_count} application email(s)!")
