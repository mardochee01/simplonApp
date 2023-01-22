from django.core import validators
from django import forms
from .models import Participant
from phonenumber_field.widgets import PhoneNumberPrefixWidget

class ParticipantRegistration(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['lastName', 'firstName', 'phoneNumber', 'email']
        widgets = {
            'lastName': forms.TextInput(attrs={'class': 'form-control'}),
            'firstName': forms.TextInput(attrs={'class': 'form-control'}),
            'phoneNumber': PhoneNumberPrefixWidget(initial='CI', attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }