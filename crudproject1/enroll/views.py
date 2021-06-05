from django.shortcuts import render, HttpResponseRedirect
from .forms import AddProduct
from .models import Products
# Create your views here.
def add_show(request):
    if request.method == 'POST':
        p1 = AddProduct(request.POST)
        if p1.is_valid():
            # p2 = AddProduct(name=p1.cleaned_data['name'],
            #     type=p1.cleaned_data['type'],
            #     category=p1.cleaned_data['category']
            # )
            p1.save()
            p1 = AddProduct()

    else:
        p1 = AddProduct()
    products = Products.objects.all()
    print(dir(products))
    return render(request, 'enroll/view_products.html', {'form':p1,'prod':products})

def delete_product(request, id):
    if request.method == 'POST':
        p = Products.objects.get(pk=id)
        p.delete()
        return HttpResponseRedirect('/')

def update_product(request, id):
    if request.method == 'POST':
        p = Products.objects.get(pk=id)
        form_obj = AddProduct(request.POST, instance=p)
        if form_obj.is_valid():
            form_obj.save()
    else:
        p = Products.objects.get(pk=id)
        form_obj = AddProduct(instance=p)
    return render(request, 'enroll/update_product.html', {'form':form_obj})
