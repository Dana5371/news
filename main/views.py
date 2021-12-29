from django.db import models
from main.models import Post
from django.views.generic import ListView



class HomePageView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'
    

