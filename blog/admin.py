from django.contrib import admin
from django.utils.html import format_html
from unfold.admin import ModelAdmin
from blog.models import Post, Category

@admin.register(Post)
class PostAdmin(ModelAdmin):
    list_display = ('title', 'display_image', 'get_categories', 'date')
    search_fields = ('title', 'summary', 'content')
    list_filter = ('date', 'categories')
    filter_horizontal = ('categories',)

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="60" height="auto" style="border-radius: 5px;" />', obj.image.url)
        return "No Image"
    display_image.short_description = 'Preview'

    def get_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all()])
    get_categories.short_description = 'Categories'


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

