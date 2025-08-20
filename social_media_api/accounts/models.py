from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    following = models.ManyToManyField(
       "self",  # self-referential
        symmetrical=False,  # following is one-directional
        related_name="followers",  # reverse relation
        blank=True 
    )

    def __str__(self):
        return self.username

