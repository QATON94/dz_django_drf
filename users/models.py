from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='email')
    phone = models.CharField(max_length=20, unique=True, verbose_name='phone')
    city = models.CharField(max_length=50, unique=True, verbose_name='city')
    avatar = models.ImageField(upload_to='avatars', default='avatars/default.png', verbose_name='аватар')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return self.email
