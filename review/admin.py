from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'paper', 'star', 'commit', 'created_at')
    search_fields = ('paper__name', 'commit')
    list_filter = ('star', 'created_at')
    ordering = ('-created_at',)
