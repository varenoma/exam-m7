from django.contrib import admin
from .models import Paper


@admin.register(Paper)
class PaperAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author', 'is_verified',
                    'view_count', 'created_at')
    list_filter = ('is_verified', 'created_at', 'author')
    search_fields = ('name', 'author__username', 'keyword', 'annotation')
    ordering = ('-created_at',)
