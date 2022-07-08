from django.shortcuts import render, reverse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import CreateView
from django.http.response import HttpResponse
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from .models import Customer

def index(req):
    return HttpResponse('Hello there')

# Create your views here
class CustomerDetailView(DetailView):
    model = Customer

class CustomerListView(ListView):
    model = Customer

class CustomerCreateView(CreateView):
    model = Customer
    fields = '__all__'

class CustomerUpdateView(UpdateView):
    model = Customer
    fields = '__all__'

class CustomerDeleteView(DeleteView):
    model = Customer
    success_url = '/customer/list' # todo: dynamic url

