from django.contrib import admin

from .models import Tweet


@admin.register(Tweet)
class TagAdmin(admin.ModelAdmin):
    list_display = ['user', 'body', 'created_at', 'updated_at']