# journal.models.py
from django.db import models

from account.models import User

# Create your models here.


class Journal(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    pdf = models.FileField(upload_to='journal/pdf/')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='journal_author')
    technologies = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='journal/avatar/')
    view_count = models.PositiveIntegerField(default=0)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'journal'
