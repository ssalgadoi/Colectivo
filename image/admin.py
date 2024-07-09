from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Post, PostImage


class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 1


@admin.register(Post)
class PostAdmin(TranslatableAdmin):
    list_display = ['title', 'author', 'published']
    ordering = ['-published']
    search_fields = ['translations__title', 'translations__content']
    date_hierarchy = 'published'
    list_filter = ['author', 'created', 'updated']

    inlines = [PostImageInline]

    fieldsets = (
        (None, {
            'fields': ('title', 'content', 'published')
        }),
        ('Media', {
            'fields': ('image',),
        }),
        ('Meta', {
            'fields': ('author', 'created', 'updated'),
            'classes': ('collapse',),
        }),
    )

    readonly_fields = ('created', 'updated')


admin.site.register(PostImage)
