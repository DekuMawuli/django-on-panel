from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    is_voter = models.BooleanField(default=False)
    is_election_admin = models.BooleanField(default=False)
    is_system_admin = models.BooleanField(default=False)
    phone = models.CharField(max_length=20, blank=True, null=True)
