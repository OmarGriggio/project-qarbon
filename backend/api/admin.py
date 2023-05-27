from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from .models import Message, Event, Place, Comment, Rating

@admin.register(Message)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('pk', 'subject', 'created_at', 'updated_at')
    list_filter = ('created_at',)
    search_fields = ('subject', 'body')

@admin.register(Event)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'date', 'place', 'image', 'user')
    list_filter = ('date',)
    search_fields = ('name', 'description')

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'locality')
    search_fields = ('name', 'locality')

# Unregister the default User admin
admin.site.unregister(User)

@admin.register(User)
class UserAdmin(DefaultUserAdmin):
    list_display = ('pk', 'username', 'email')
    search_fields = ('username', 'email')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'user', 'place')
    search_fields = ('text', 'user', 'place')

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('pk', 'rating', 'place', 'rated_by')
    search_fields = ('rating', 'place', 'rated_by')