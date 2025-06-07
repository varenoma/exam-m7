from django.contrib import admin

from .models import Journal

# Register your models here.


@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author', 'is_verified',
                    'view_count', 'created_at')
    list_filter = ('is_verified', 'created_at')
    search_fields = ('name', 'author__username', 'technologies')
    readonly_fields = ('view_count', 'created_at')
