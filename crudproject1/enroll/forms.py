from django.core import validators
from django import forms
from django.db.models import fields
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class':"form-control"}),            
        }

class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class':"form-control"}),            
        }

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class':"form-control"}),            
        }

class FabricForm(forms.ModelForm):
    class Meta:
        model = Fabric
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class':"form-control"}),            
        }

class ReturnPolicyForm(forms.ModelForm):
    class Meta:
        model = ReturnPolicy
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class':"form-control"}),            
        }        

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user