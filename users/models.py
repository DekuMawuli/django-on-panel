from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    is_voter = models.BooleanField(default=False)
    is_election_admin = models.BooleanField(default=False)
    is_system_admin = models.BooleanField(default=False)
    phone = models.CharField(max_length=20, blank=True, null=True)
    has_voted = models.BooleanField(default=False)


class ElectionAdminProfile(models.Model):
    election_admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    number_of_election = models.IntegerField(default=1)
