#NAME: LEE KEI KAR
#STUDENT ID: 23100598

from django.contrib import admin
from .models import User, DisasterReport, AidRequest, Shelter
from django.contrib.auth.admin import UserAdmin

admin.site.register(User, UserAdmin)
admin.site.register(DisasterReport)
admin.site.register(AidRequest)
admin.site.register(Shelter)

