#NAME: LEE KEI KAR
#STUDENT ID: 23100598


from django.db import models
from django.utils import timezone

class VolunteerSkill(models.Model):
    name = models.CharField(max_length=100)  # The user's name or ID (can link to auth.User later)
    skill = models.CharField(max_length=100)
    availability = models.CharField(max_length=100)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} – {self.skill}"

class VolunteerAssignment(models.Model):
    volunteer = models.ForeignKey(VolunteerSkill, on_delete=models.CASCADE)
    task = models.CharField(max_length=255, default='General')
    assigned_at = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return f"{self.volunteer.name} - {self.task}"