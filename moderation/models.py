# moderation.models.py
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.forms import ValidationError

from account.models import User
from paper.models import Paper
from journal.models import Journal

# Create your models here.


class Moderation(models.Model):
    description = models.TextField()
    star = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)])
    reviewer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviewer_reviews'
    )
    paper = models.ForeignKey(
        Paper, on_delete=models.SET_NULL, null=True, blank=True)
    journal = models.ForeignKey(
        Journal, on_delete=models.SET_NULL, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        super().clean()
        if not self.paper and not self.journal:
            raise ValidationError(
                "Paper, Journal yoki Moderationdan birini tanlashingiz shart")

    def __str__(self):
        return self.reviewer.username if self.reviewer else "Reviewer o'chirilgan"

    class Meta:
        db_table = 'moderation'
