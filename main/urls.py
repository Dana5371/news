from django.urls import path

from main.views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='homepage')

]