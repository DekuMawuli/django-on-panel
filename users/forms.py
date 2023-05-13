from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = [
            "first_name", "last_name", "username", "email",
            "is_voter", "is_election_admin", "is_system_admin",
            "phone", "password1", "password2"
        ]


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = [
            "first_name", "last_name", "username", "email",
            "is_voter", "is_election_admin", "is_system_admin",
            "phone"
        ]