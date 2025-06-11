# review/admin.py
from django.contrib import admin
from .models import Moderation


@admin.register(Moderation)
class ModerationAdmin(admin.ModelAdmin):
    list_display = ('id', 'moder', 'star', 'created_at', 'is_verified')
    search_fields = ('moder__username', 'description')
    list_filter = ('star', 'created_at', 'is_verified')
