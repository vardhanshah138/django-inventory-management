from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Products)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Supplier)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(SubCategory)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Brand)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Fabric)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(TaxClass)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(ReturnPolicy)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(ProductImage)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Inventory)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Profile)
class UserAdmin(admin.ModelAdmin):
    pass
