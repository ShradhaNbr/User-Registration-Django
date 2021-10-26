from django.contrib.auth.models import User

from django.db import models


# Create your models here.


class Notes(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=True)
