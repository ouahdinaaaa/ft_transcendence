from django.contrib.auth.models import AbstractUser
from django.db import models

class AddUserFirst(AbstractUser):
    intra_id = models.IntegerField(unique=True, null=True, blank=True)  # Identifiant unique optionnel
    intra_email = models.EmailField(null=True, blank=True)  # Email optionnel
    profile_picture = models.URLField(null=True, blank=True)  # URL pour une photo de profil optionnelle

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # Évite les conflits avec le modèle User par défaut
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set',  # Évite les conflits avec le modèle User par défaut
        blank=True
    )

class Band(models.Model):
    name = models.CharField(max_length=100)  # Nom du groupe
