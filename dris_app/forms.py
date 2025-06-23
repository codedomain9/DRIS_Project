#NAME: LEE KEI KAR
#STUDENT ID: 23100598


from django import forms
from .models import AidRequest
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class AidRequestForm(forms.ModelForm):
    class Meta:
        model = AidRequest
        fields = ['aid_type', 'description']

class DisasterFilterForm(forms.Form):
    disaster_type = forms.CharField(max_length=50, required=False, label='Filter by Disaster Type')

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)