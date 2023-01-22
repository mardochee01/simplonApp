from django.contrib import admin
from .models import Participant
from django import forms
from phonenumber_field.widgets import PhoneNumberPrefixWidget

class ParticipantForm(forms.ModelForm):
    class Meta:
        widgets = {
            'phoneNumber': PhoneNumberPrefixWidget(initial='CI'),
        }

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('id', 'lastName', 'firstName', 'phoneNumber', 'email')
    form = ParticipantForm