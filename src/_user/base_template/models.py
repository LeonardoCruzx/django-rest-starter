from .manager import UserManager

from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    objects = UserManager()