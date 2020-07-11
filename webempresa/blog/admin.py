from django.contrib import admin
from .models import Category, Post

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)
    

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)
    list_display = ('title', 'author', 'published', 'Post_categories')
    ordering = ('author', 'published')
    search_fields = ('title','content', 'author__username', 'categories__name')
    date_hierarchy = 'published'
    list_filter = ('author__username','categories__name')

    def Post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by('name')])

    Post_categories.short_description = 'Categorías'

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
