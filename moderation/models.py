# moderation.models.py
from django.db import models

from account.models import User
from paper.models import Paper
from review.models import Review

# Create your models here.


class Moderation(models.Model):
    review = models.ForeignKey(
        Review, on_delete=models.SET_NULL, related_name='moderation_review', null=True)
    paper = models.ForeignKey(Paper, on_delete=models.SET_NULL, null=True)
    moder = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    star = models.PositiveIntegerField(default=0)
    commit = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.moder.username if self.moder else "Moder o'chirilgan"

    class Meta:
        db_table = 'moderation'
