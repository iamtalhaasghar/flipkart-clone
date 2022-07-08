from django.urls import path
from . import views

urlpatterns=[
    path('', views.index),
    path('detail/<int:pk>', views.CustomerDetailView.as_view(), name='customer-detail'),
    path('list/', views.CustomerListView.as_view(), name='customer-list'),
    path('create/', views.CustomerCreateView.as_view(), name='customer-create'),
    path('update/<int:pk>', views.CustomerUpdateView.as_view(), name='customer-update'),
    path('delete/<int:pk>', views.CustomerDeleteView.as_view(), name='customer-delete'),
]