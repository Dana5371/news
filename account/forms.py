from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.db import transaction
from django.forms.fields import ChoiceField
from account.models import Doctor, Patient, User

class DoctorSignUpForm(UserCreationForm):
    DEPARTMENT = (
        ('cardiology', 'Cardiology'),        
        ('neurology', 'Neurology'),
        ('surgeon', 'Surgeon'),
        ('allergist', 'Allergist'),
        ('therapist', 'Therapist'),
        ('psychologist', 'Psychologist')
    )
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=14)
    department = forms.ChoiceField(choices=DEPARTMENT)


    

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def data_save(self):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data.get('fisrt_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        doctor = Doctor.objects.create(user=user)
        doctor.email = self.cleaned_data.get('email')
        doctor.phone_number = self.cleaned_data('phone_number')
        doctor.depatment = self.cleaned_data('department')
        doctor.save()
        return user


class PatientSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField()
    location = forms.CharField(max_length=14)

    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def data_save(self):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data.get('fisrt_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        patient = Patient.objects.create(user=user)
        patient.email = self.cleaned_data.get('email')
        patient.location = self.cleaned_data('location')
        patient.save()
        return user