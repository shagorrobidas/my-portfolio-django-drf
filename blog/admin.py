from django.contrib import admin
from blog.models import Post, Category

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_categories', 'date')
    search_fields = ('title',)
    list_filter = ('date', 'categories')
    filter_horizontal = ('categories',)

    def get_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all()])
    get_categories.short_description = 'Categories'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

