from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from .forms import UserForm

User = get_user_model()

# Create your views here.
class SignUp(generic.CreateView):
    model = User
    template_name = 'accounts/sign_up.html'
    form_class = UserForm
    success_url = reverse_lazy('accounts:login')
    

class ProfilePage(generic.DetailView):
    model = User
    template_name = 'accounts/profile.html'
    




