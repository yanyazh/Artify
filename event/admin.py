from django.contrib import admin
from .models import Event

# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'description')  # Customize the list display columns
    search_fields = ('title', 'description')  # Add fields to search in admin interface
    list_filter = ('date',)  # Add filters in admin interface

admin.site.register(Event)