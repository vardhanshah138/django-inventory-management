from django.db import models
from phonenumber_field.modelfields import PhoneNumberField



# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=70)
    type = models.CharField(max_length=100)
    category = models.CharField(max_length=70)

class Supplier(models.Model):
    name = models.CharField(max_length=70)
    phone = PhoneNumberField()

    