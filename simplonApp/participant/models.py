from django.db import models
# from django.core.validators import RegexValidator
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Participant(models.Model):
    lastName = models.CharField(max_length=100)
    firstName = models.CharField(max_length=100)
    # phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    # phoneNumber = models.CharField(validators = [phoneNumberRegex], max_length = 16, unique = True)
    phoneNumber = PhoneNumberField()
    email = models.EmailField()

    def __str__(self):
        return self.lastName + " " + self.firstName
