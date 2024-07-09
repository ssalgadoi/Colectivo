from django.contrib import admin
from .models import Contact


# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'created')
    search_fields = ('name', 'email', 'message', 'created')
    list_filter = ('created',)

admin.site.register( Contact , ContactAdmin )
