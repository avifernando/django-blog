from django.shortcuts import render
from django.views.generic import ListView
from .models import entry

# Create your views here.
class HomeView(ListView):
    model = entry
    template_name='entries/index.html'