from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.urls import reverse_lazy

# Create your models here.
from django.views import generic

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
