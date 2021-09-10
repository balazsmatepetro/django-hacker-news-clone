from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    about = models.TextField(blank=True, default='')

    class Meta:
        db_table = 'auth_user'

    @staticmethod
    def get_by_username(username: str):
        return User.objects.get(username=username)
