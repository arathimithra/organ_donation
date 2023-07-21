from django.contrib.auth.models import User
from django.db import models

# Create your models here.




class Donor(models.Model):

    name = models.CharField(max_length=500)
    age = models.CharField(max_length=100)
    gender =models.CharField(max_length=100)
    blood_group = models.CharField(max_length=100)
    organ = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    status = models.BooleanField()

    def __str__(self):
        return self.name

class BloodDonor(models.Model):

    name = models.CharField(max_length=500)
    age = models.CharField(max_length=100)
    gender =models.CharField(max_length=100)
    blood_group = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    status = models.BooleanField()

    def __str__(self):
        return self.name