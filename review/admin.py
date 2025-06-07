from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'reviewer', 'star', 'created_at')
    list_filter = ('star', 'created_at')
    search_fields = ('reviewer__username', 'description')
    ordering = ('-created_at',)
