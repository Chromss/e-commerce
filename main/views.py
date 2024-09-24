from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from main.models import Product
from main.forms import ProductForm

def show_main(request):
    return render(request, 'main.html')

def show_add_inventory(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            product = product_form.save(commit=False)
            product.variation_count = int(request.POST.get('countVar'))
            product.minimum_price = int(request.POST.get('minPrice'))
            product.save()
    else:
        product_form = ProductForm()

    return render(request, 'add-inventory.html', {
        'product_form': product_form,
    })


def show_product(request):
    products = Product.objects.all()
    return render(request, 'product.html', {'products': products})

def show_login(request):
    return render(request, 'login.html')

def show_signup(request):
    return render(request, 'signup.html')

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")