from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm

from account.models import Doctor, Patient, User

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(User)