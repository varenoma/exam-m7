# review.models.py
from django.db import models

from paper.models import Paper
from journal.models import Journal

# Create your models here.


class Review(models.Model):
    paper = models.ForeignKey(
        Paper, on_delete=models.SET_NULL, null=True, related_name='review_moderations', blank=True)
    journal = models.ForeignKey(
        Journal, on_delete=models.SET_NULL, null=True, related_name='review_journal', blank=True)
    star = models.PositiveIntegerField(default=0)
    commit = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.star)

    class Meta:
        db_table = 'review'
