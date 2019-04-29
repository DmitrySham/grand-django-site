from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Account(AbstractUser):
    email = models.EmailField(verbose_name='Почта', unique=True)
    username = models.CharField(max_length=255, verbose_name='Имя пользователя', null=True, blank=True, unique=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
