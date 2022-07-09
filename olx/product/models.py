from django.db import models
from django.shortcuts import reverse

# Create your models here.

class Product(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product-detail", kwargs={"pk": self.pk})
