# account.models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator

# Create your models here.

# admin uchun username: admin, password: admin


class User(AbstractUser):
    email = models.EmailField(unique=True, validators=[EmailValidator()])
    birth_date = models.DateField(blank=True, null=True)
    organization = models.CharField(max_length=200, blank=True)
    scientific_degree = models.CharField(max_length=200, blank=True)
    another_information = models.TextField(blank=True)
    image = models.ImageField(upload_to='account/',
                              default='account/default.jpg', blank=True, null=True)
    user_verified = models.BooleanField(default=True)
    moder_verified = models.BooleanField(default=False)
    reviewer_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'user'
