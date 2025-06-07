# review.models.py
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from account.models import User

# Create your models here.


class Review(models.Model):
    description = models.TextField()
    star = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)])
    reviewer = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.reviewer.username if self.reviewer else "Reviewer o'chirilgan"

    class Meta:
        db_table = 'review'
