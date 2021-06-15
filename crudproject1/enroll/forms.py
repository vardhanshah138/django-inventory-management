from django.core import validators
from django import forms
from django.db.models import fields
from .models import Products,Supplier


class AddProduct(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name','type','category']
        widgets = {
            'name': forms.TextInput(attrs={'class':"form-control"}),
            'type': forms.TextInput(attrs={'class':"form-control"}),
            'category': forms.TextInput(attrs={'class':"form-control"})
        }

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name','phone']
        widgets = {
            'name': forms.TextInput(attrs={'class':"form-control"}),
            'phone': forms.TextInput(attrs={'class':"form-control"}),
        }