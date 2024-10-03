import datetime
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.urls import reverse
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.html import strip_tags
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from main.models import *
from main.forms import *

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
    product_form = ProductForm(request.POST, request.FILES)
    if product_form.is_valid() and request.method == "POST":
        product = product_form.save(commit=False)
        product.user = request.user
        product.variation_count = int(request.POST.get('countVar'))
        product.minimum_price = int(request.POST.get('minPrice'))
        product.save()
        return redirect('main:show_main')
    else:
        product_form = ProductForm()

    return render(request, 'add-inventory.html', {
        'product_form': product_form,
    })

@login_required(login_url='/login')
def show_product(request):
    context = {'name': request.user.username}
    return render(request, 'product.html', context)

def edit_inventory(request, id):
    product = Product.objects.get(pk=id)
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_product'))
    context = {'form': form, 'product': product}
    return render(request, "edit-inventory.html", context)

def delete_inventory(request, id):
    product = Product.objects.get(pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_product'))

@csrf_exempt
@require_POST
def add_inventory_direct(request):
    name = strip_tags(request.POST.get("name"))
    description = strip_tags(request.POST.get("description"))
    image = request.POST.get("image")
    variation_count = int(request.POST.get('countVar'))
    minimum_price = int(request.POST.get('minPrice'))
    user = request.user

    new_product = Product(name=name, description=description, image=image, variation_count=variation_count, minimum_price=minimum_price, user=user) 
    new_product.save()
    return HttpResponse(b"CREATED", status=201)

def show_xml(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")