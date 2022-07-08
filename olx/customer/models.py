from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Customer(models.Model):

    # models.fields are not same as django.forms.fields

    #username = models.CharField(max_length=256)
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name   

    def get_absolute_url(self):
        return reverse('customer-detail', kwargs={"pk": self.pk})
    