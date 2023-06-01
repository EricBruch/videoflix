from django.db import models
from django.contrib.auth.models import AbstractUser
import random
import string


# Create your models here.
class CustomUser(AbstractUser):
    custom = models.CharField(max_length=1000, default="")
    phone = models.CharField(max_length=20, default="")
    address = models.CharField(max_length=200, default="")
    resetSecret = models.CharField(
        max_length=40, default="".join(random.choices(string.ascii_letters, k=10))
    )
