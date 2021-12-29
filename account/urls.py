from django.urls import path
from .views import doctor_register, patient_register, register

urlpatterns=[
    path('register/', register, name='register'),
    path('doctor_register/', doctor_register.as_view(), name='doctor-register'),
    path('patient_register/', patient_register.as_view(), name='patient-register')
]