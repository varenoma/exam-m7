# review.models.py
from django.db import models

from paper.models import Paper
from journal.models import Journal
from account.models import User

# Create your models here.


class Review(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='review_user', blank=True)
    paper = models.ForeignKey(
        Paper, on_delete=models.SET_NULL, null=True, related_name='review_paper', blank=True)
    journal = models.ForeignKey(
        Journal, on_delete=models.SET_NULL, null=True, related_name='review_journal', blank=True)
    star = models.PositiveIntegerField(default=0)
    commit = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.star)

    class Meta:
        db_table = 'review'
