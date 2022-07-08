from django.urls import path
from .views import *
urlpatterns = [
    path("add/", ProductCreateView.as_view(), name="add_product")
]
