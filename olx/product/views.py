from django.shortcuts import render, reverse
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView

from .models import *

# Create your views here.

class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'

class ProductUpdateView(UpdateView):
    model = Product
    fields = '__all__'
    #template_name = ".html"

class ProductListView(ListView):
    model = Product
    #template_name = ".html"

class ProductDetailView(DetailView):
    model = Product
    #template_name = ".html"

class ProductDeleteView(DeleteView):
    model = Product
    success_url = '/product/list'
    #template_name = ".html"



