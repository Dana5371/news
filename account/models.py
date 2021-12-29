from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

class Doctor(models.Model):
    DEPARTMENT = (
        ('cardiology', 'Cardiology'),        
        ('neurology', 'Neurology'),
        ('surgeon', 'Surgeon'),
        ('allergist', 'Allergist'),
        ('therapist', 'Therapist'),
        ('psychologist', 'Psychologist')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=14)
    department = models.CharField(choices=DEPARTMENT, max_length=55)

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=14)
    location = models.CharField(max_length=55)
    


