from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=70)
    type = models.CharField(max_length=100)
    category = models.CharField(max_length=70)