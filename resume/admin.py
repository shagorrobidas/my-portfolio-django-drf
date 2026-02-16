from django.contrib import admin
from resume.models import Education, Experience, Skill


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'start_date', 'end_date', 'order')
    list_editable = ('order',)
    list_filter = ('institution', 'degree')
    search_fields = ('institution', 'degree', 'description')
    ordering = ('order', '-start_date')


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('role', 'company', 'start_date', 'end_date', 'order')
    list_editable = ('order',)
    list_filter = ('company',)
    search_fields = ('role', 'company', 'description')
    ordering = ('order', '-start_date')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'proficiency')
    list_editable = ('proficiency',)
    search_fields = ('name',)
    ordering = ('-proficiency', 'name')
