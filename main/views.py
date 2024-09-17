from django.shortcuts import render, redirect
from main.models import Product
from main.forms import ProductForm

def show_main(request):
    return render(request, 'main.html')

def show_add_inventory(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            product = product_form.save(commit=False)
            product.variation_count = int(request.POST.get('countVar', 0))
            product.average_price = int(request.POST.get('averageVal', 0))
            
            product.save()
            return redirect('main:show_product')
    else:
        product_form = ProductForm()

    return render(request, 'add-inventory.html', {
        'product_form': product_form,
    })


def show_product(request):
    products = Product.objects.all()
    return render(request, 'product.html', {'products': products})