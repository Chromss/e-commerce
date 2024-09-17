from django import forms
from .models import Product, Variation

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image']

class VariationForm(forms.ModelForm):
    class Meta:
        model = Variation
        fields = ['variation_type', 'price']