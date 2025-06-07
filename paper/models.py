# paper.models.py
from django.db import models

from account.models import User

# Create your models here.


class Paper(models.Model):
    name = models.CharField(max_length=150)
    annotation = models.TextField()
    keyword = models.TextField()
    article = models.TextField()
    reference = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='paper_author')
    view_count = models.PositiveIntegerField(default=0)
#    review = models.ForeignKey(
#        Review, on_delete=models.SET_NULL, null=True, blank=True, related_name='paper_review')
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} | {self.is_verified}"

    class Meta:
        db_table = 'paper'
