# review/admin.py
from django.contrib import admin
from .models import Moderation


@admin.register(Moderation)
class ModerationAdmin(admin.ModelAdmin):
    list_display = ('id', 'reviewer', 'star', 'created_at')
    search_fields = ('reviewer__username', 'description')
    list_filter = ('star', 'created_at')
