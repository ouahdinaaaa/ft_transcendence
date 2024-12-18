from django.db import models
from django.contrib.auth.models import AbstractUser

class AddUserFirst(AbstractUser):
    intra_id = models.IntegerField(unique=True, null=True, blank=True)
    intra_email = models.EmailField(null=True, blank=True)
    profile_picture = models.URLField(null=True, blank=True)
    additional_field = models.CharField(max_length=100, blank=True, null=True)

class Band(models.Model):
    name = models.CharField(max_length=100)  # Petite correction ici
