#NAME: LEE KEI KAR
#STUDENT ID: 23100598

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('citizen', 'Citizen'),
        ('volunteer', 'Volunteer'),
        ('authority', 'Authority'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

class DisasterReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    disaster_type = models.CharField(max_length=50)
    gps_coordinates = models.CharField(max_length=100)
    severity = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)

class AidRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    aid_type = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Shelter(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    capacity = models.IntegerField()
    available_space = models.IntegerField()

    def __str__(self):
        return self.name




