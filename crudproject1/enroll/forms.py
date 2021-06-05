from django.core import validators
from django import forms
from .models import Products


class AddProduct(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name','type','category']
        widgets = {
            'name': forms.TextInput(attrs={'class':"form-control"}),
            'type': forms.TextInput(attrs={'class':"form-control"}),
            'category': forms.TextInput(attrs={'class':"form-control"})
        }