from django.contrib import admin

from .models import Message, Event

@admin.register(Message)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('pk', 'subject', 'created_at', 'updated_at')
    list_filter = ('created_at',)
    search_fields = ('subject', 'body')

@admin.register(Event)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'date', 'place', 'user')
    list_filter = ('date',)
    search_fields = ('name', 'description')
