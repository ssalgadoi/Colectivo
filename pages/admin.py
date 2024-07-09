from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Page

class PageAdmin(TranslatableAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'order')

admin.site.register(Page, PageAdmin)