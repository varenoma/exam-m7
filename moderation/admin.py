from django.contrib import admin
from .models import Moderation


@admin.register(Moderation)
class ModerationAdmin(admin.ModelAdmin):
    list_display = ('id', 'moder', 'paper', 'review',
                    'star', 'created_at')
    list_filter = ('moder', 'star', 'created_at')
    search_fields = ('moder__username', 'paper__name',
                     'review__description')
    readonly_fields = ('created_at',)
