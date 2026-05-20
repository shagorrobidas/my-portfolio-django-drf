from django.contrib import admin
from django.utils.html import format_html
from unfold.admin import ModelAdmin, TabularInline
from main.models import (
    ContactMessage,
    Profile,
    ProfileSection,
    ProfileTitle,
    Service,
    Testimonial,
    Client,
    SocialLink
)

# ... (rest unchanged, skipping registration declarations for Client and SocialLink) ...


@admin.register(Client)
class ClientAdmin(ModelAdmin):
    list_display = ('name', 'url', 'display_logo', 'order')
    list_editable = ('order',)
    search_fields = ('name',)

    def display_logo(self, obj):
        if obj.logo:
            return format_html('<img src="{}" width="50" height="auto" style="border-radius: 5px;" />', obj.logo.url)
        return "No Logo"
    display_logo.short_description = 'Logo Preview'

@admin.register(SocialLink)
class SocialLinkAdmin(ModelAdmin):
    list_display = ('name', 'url', 'display_icon', 'order')
    list_editable = ('order',)
    search_fields = ('name',)

    def display_icon(self, obj):
        return format_html('<i class="{}"></i>', obj.icon)
    display_icon.short_description = 'Icon'

class ProfileSectionInline(TabularInline):
    model = ProfileSection
    extra = 1
    fields = ('title', 'content', 'order')


class ProfileTitleInline(TabularInline):
    model = ProfileTitle
    extra = 1
    fields = ('title', 'order')


@admin.register(Profile)
class ProfileAdmin(ModelAdmin):
    list_display = ('name', 'title', 'email', 'display_avatar')
    list_filter = ('name',)
    search_fields = ('name', 'title', 'email')
    ordering = ('name',)
    inlines = [ProfileTitleInline, ProfileSectionInline]

    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'title', 'avatar', 'birthday', 'location')
        }),
        ('Contact Information', {
            'fields': ('email', 'linkedin_username', 'linkedin_url', 'github_username', 'github_url')
        }),
        ('About Me', {
            'fields': ('about_text', 'about_text_extra')
        }),
    )

    def display_avatar(self, obj):
        if obj.avatar:
            return format_html('<img src="{}" width="40" height="40" style="border-radius: 50%;" />', obj.avatar.url)
        return "No Avatar"
    display_avatar.short_description = 'Avatar'

@admin.register(Service)
class ServiceAdmin(ModelAdmin):
    list_display = ('title', 'display_icon', 'description')
    list_filter = ('title',)
    search_fields = ('title', 'description')
    ordering = ('title',)

    def display_icon(self, obj):
        return format_html('<i class="{}"></i>', obj.icon_class)
    display_icon.short_description = 'Icon'

@admin.register(Testimonial)
class TestimonialAdmin(ModelAdmin):
    list_display = ('client_name', 'display_image', 'text')
    list_filter = ('client_name',)
    search_fields = ('client_name', 'text')
    ordering = ('client_name',)

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="40" height="40" style="border-radius: 50%;" />', obj.image.url)
        return "No Image"
    display_image.short_description = 'Image'

@admin.register(ContactMessage)
class ContactMessageAdmin(ModelAdmin):
    list_display = ('full_name', 'email', 'subject', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('full_name', 'email', 'message', 'subject')
    ordering = ('-created_at',)
    readonly_fields = ('full_name', 'email', 'subject', 'message', 'created_at')
