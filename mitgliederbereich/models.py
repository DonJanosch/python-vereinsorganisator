from django.db import models
from phone_field import PhoneField

# Create your models here.
class Mitglied(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    phone = PhoneField(blank=True, help_text='Contact phone number')


class Windenfahrer(models.Model):
    mitglied = models.ForeignKey(Mitglied, on_delete=models.CASCADE)
    is_EWF = models.BinaryField(default=False)
