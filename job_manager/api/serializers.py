from rest_framework import serializers
from job_manager.models import JobApplication

class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = [
            'id', 'company_name', 'job_title', 'employer_email', 
            'job_description_text', 'job_description_image',
            'generated_cv', 'generated_cover_letter',
            'cv_pdf', 'cv_word', 'cover_letter_pdf', 'cover_letter_word',
            'status', 'created_at'
        ]
        read_only_fields = [
            'generated_cv', 'generated_cover_letter',
            'cv_pdf', 'cv_word', 'cover_letter_pdf', 'cover_letter_word',
            'status', 'created_at'
        ]
