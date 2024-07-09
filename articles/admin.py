from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Post

@admin.register(Post)
class PostAdmin(TranslatableAdmin):
    list_display = ('title', 'author', 'published', 'created', 'updated')
    list_filter = ('published', 'created', 'updated', 'translations__title')
    search_fields = ('translations__title', 'translations__content')
    
    fieldsets = (
        (None, {
            'fields': ('title', 'content', 'published', 'image', 'url_link', 'author')
        }),
    )



    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)
