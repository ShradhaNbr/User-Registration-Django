from django.contrib.auth.models import models, User


# Create your models here.


class UserRegistration(User):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    state = models.CharField(max_length=100)