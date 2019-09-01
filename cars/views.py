from django.shortcuts import render

from django.views.generic import ListView

from .models import Car

# Create your views here.
class CarListView(ListView):
    model = Car
    context_object_name = 'cars'