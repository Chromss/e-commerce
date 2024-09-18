from django.forms import ModelForm, IntegerField
from main.models import Product

class ProductForm(ModelForm):
    variation_count = IntegerField(required=False, initial=0)
    minimum_price = IntegerField(required=False, initial=0)

    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'variation_count', 'minimum_price']