from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

class spartanews(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
