#NAME: LEE KEI KAR
#STUDENT ID: 23100598

from django.contrib import admin
from .models import VolunteerSkill
from .models import VolunteerAssignment

admin.site.register(VolunteerSkill)
admin.site.register(VolunteerAssignment)
