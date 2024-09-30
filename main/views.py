import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from main.models import *
from main.forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

def show_main(request):
    context = {'last_login': request.COOKIES.get('last_login', 'None')}
    return render(request, 'main.html', context)

def show_signup(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:show_login')
        else:
            print(form.errors)
    context = {'form': form}
    return render(request, 'signup.html', context)

def show_login(request):
    form = AuthenticationForm(request)
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
            return response
    context = {'form': form}
    return render(request, 'login.html', context)

def do_logout(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:show_main'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/login')
def show_add_inventory(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            product = product_form.save(commit=False)
            product.user = request.user  # Assign the current user here
            product.variation_count = int(request.POST.get('countVar'))
            product.minimum_price = int(request.POST.get('minPrice'))
            product.save()  # Save the product with the user assigned
            return redirect('main:show_main')  # Optionally redirect after saving
    else:
        product_form = ProductForm()

    return render(request, 'add-inventory.html', {
        'product_form': product_form,
    })

@login_required(login_url='/login')
def show_product(request):
    form = ProductForm(request.POST or None)
    
    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return redirect('main:show_main')
    
    current_user = Product.objects.filter(user=request.user)
    context = {'form': form, 'name': request.user.username,'products': Product.objects.all()}
    return render(request, 'product.html', context)

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