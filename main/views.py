from django.shortcuts import render, redirect
from main.models import Product, Variation
from main.forms import ProductForm, VariationForm

def show_main(request):
    return render(request, 'main.html')

def show_add_inventory(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            product = product_form.save()
            variation_form = VariationForm(request.POST)
            if variation_form.is_valid():
                variation = variation_form.save(commit=False)
                variation.product = product
                variation.save()
            return redirect('main:show_product')
    else:
        product_form = ProductForm()
        variation_form = VariationForm()

    return render(request, 'add-inventory.html', {
        'product_form': product_form,
        'variation_form': variation_form
    })

def show_product(request):
    products = Product.objects.all()
    return render(request, 'product.html', {'products': products})