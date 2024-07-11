from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import  Post
from django.utils.translation import gettext_lazy as _



# Admin para Valle
@admin.register(Post)
class PostAdmin(TranslatableAdmin):
    list_display = ['title', 'published', 'author', 'created', 'updated']
    search_fields = ['translations__title', 'translations__description', 'translations__content', 'translations__data']
    ordering = ['-published']
    fieldsets = [
        (None, {'fields': ['title', 'description', 'content', 'data']}),
        (_('Publication'), {'fields': ['published']}),
        (_('Media'), {'fields': ['image', 'video']}),
        (_('Relationships'), {'fields': ['author']}),
    ]

    def get_queryset(self, request):
        return super().get_queryset(request).translated()