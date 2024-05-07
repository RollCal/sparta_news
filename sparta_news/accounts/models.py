from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
<<<<<<< HEAD
    pass

=======
    created_at = models.DateTimeField(auto_now_add=True)
>>>>>>> 9813829457e85f4ec2966711c2eeae49790eaf0a
