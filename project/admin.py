from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Post

@admin.register(Post)
class PostAdmin(TranslatableAdmin):
    list_display = ('title', 'author', 'published', 'created')
    list_filter = ('author', 'published', 'created')
    search_fields = ('translations__title', 'author__username')
    
    fieldsets = (
        (None, {
            'fields': ('title', 'content', 'image', 'url_link', 'author', 'published')
        }),
        ('Fechas', {
            'fields': ('created', 'updated'),
        }),
    )
    
    readonly_fields = ('created', 'updated')