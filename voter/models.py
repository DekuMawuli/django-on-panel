from django.db import models
from users.models import ElectionAdminProfile, CustomUser


class Timestamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Election(Timestamp):
    admin = models.ForeignKey(ElectionAdminProfile, on_delete=models.DO_NOTHING, related_name="elections")
    name = models.CharField(max_length=100, unique=True)
    schedule_date = models.DateField()
    scheduled_time = models.TimeField()
    is_open = models.BooleanField(default=False)
    banner = models.ImageField(upload_to="banner/", blank=True, null=True)

    def __str__(self):
        return self.name


class Position(Timestamp):
    election = models.ForeignKey(Election, on_delete=models.CASCADE, related_name="positions")
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.election.name} - {self.name}"


class Aspirant(Timestamp):
    position = models.ForeignKey(Position, on_delete=models.CASCADE, related_name="aspirants")
    full_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="aspirants/")
    voters = models.ManyToManyField(CustomUser, through="Vote", related_name="voters")

    def __str__(self):
        return f"{self.position.election.name} {self.position.name} - {self.full_name}"


class Vote(Timestamp):
    voter = models.ForeignKey(CustomUser, related_name="votes", on_delete=models.CASCADE)
    aspirant = models.ForeignKey(Aspirant, related_name="aspirants", on_delete=models.CASCADE)
    value = models.IntegerField(default=1)

