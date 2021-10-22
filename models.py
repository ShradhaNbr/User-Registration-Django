from django.db import models
from django.contrib.auth.models import models

# Create your models here.


class UserRegistration(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


