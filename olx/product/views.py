from django.shortcuts import render
from django.views.generic import CreateView

from .models import *

# Create your views here.

class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'
