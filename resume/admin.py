from django.contrib import admin
from resume.models import Education, Experience, Skill


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'start_date', 'end_date')
    list_filter = ('institution', 'degree')
    search_fields = ('institution', 'degree', 'field_of_study')
    ordering = ('-start_date',)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('company', 'start_date', 'end_date')
    list_filter = ('company',)
    search_fields = ('company', 'description')
    ordering = ('-start_date',)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'proficiency')
    search_fields = ('name',)
    ordering = ('name',)
