from rest_framework import serializers
from resume.models import Experience


class ExperienceSerializer(serializers.ModelSerializer):
    date_range = serializers.SerializerMethodField()

    class Meta:
        model = Experience
        fields = '__all__'
        read_only_fields = ('id',)

    def get_date_range(self, obj):
        return f"{obj.start_date} - {obj.end_date or 'Present'}"