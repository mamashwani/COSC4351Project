# Users/models.py
from django.contrib.auth.models import AbstractUser
from django import forms
from django.db import models

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(default=0)
    group_name = models.CharField(max_length=50,default='null')