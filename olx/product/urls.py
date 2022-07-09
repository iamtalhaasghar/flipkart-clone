from django.urls import path
from .views import *
urlpatterns = [
    path("create/", ProductCreateView.as_view(), name="product-create"),
    path('update/<int:pk>', ProductUpdateView.as_view(), name='product-update'),
    path("delete/<int:pk>", ProductDeleteView.as_view(), name="product-delete"),
    path("detail/<int:pk>", ProductDetailView.as_view(), name="product-detail"),  
    path("list/", ProductListView.as_view(), name="product-list"),

]
