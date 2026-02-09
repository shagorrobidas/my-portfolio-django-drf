from django.contrib import admin
from main.models import (
    ContactMessage, 
    Profile, 
    Service, 
    Testimonial,
    Client,
    SocialLink
)

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'order')
    list_editable = ('order',)
    search_fields = ('name',)

@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'order')
    list_editable = ('order',)
    search_fields = ('name',)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'email')
    list_filter = ('name',)
    search_fields = ('name', 'title', 'email')
    ordering = ('name',)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    list_filter = ('title',)
    search_fields = ('title', 'description')
    ordering = ('title',)

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'client_initials', 'text')
    list_filter = ('client_name',)
    search_fields = ('client_name', 'client_initials', 'text')
    ordering = ('client_name',)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('full_name', 'email', 'message')
    ordering = ('-created_at',)
