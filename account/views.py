from django.shortcuts import render
from django.views.generic import CreateView

from account.forms import DoctorSignUpForm, PatientSignUpForm
from .models import User

def register(request):
    return render(request, 'register.html', locals())

class doctor_register(CreateView):
    model = User
    form_class = DoctorSignUpForm
    template_name = 'doctor_register.html'

class patient_register(CreateView):
    model = User
    form_class = PatientSignUpForm
    template_name = 'patient_register.html'