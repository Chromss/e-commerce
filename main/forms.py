import re
from django.forms import *
from main.models import Product
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class ProductForm(ModelForm):
    variation_count = IntegerField(required=False, initial=0)
    minimum_price = IntegerField(required=False, initial=0)

    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'variation_count', 'minimum_price']

class UserForm(UserCreationForm):
    fullname = CharField(required=True, initial="")
    username = CharField(required=True, initial="")
    password1 = CharField(required=True, widget=PasswordInput)
    password2 = CharField(required=True, widget=PasswordInput)

    class Meta:
        model = User
        fields = ['fullname', 'username', 'password1', 'password2']

    def clean_fullname(self):
        fullname = self.cleaned_data.get('fullname')
        if len(fullname) < 10:
            raise forms.ValidationError("Minimum 10 characters.")
        if not re.match(r'^[A-Za-z ]+$', fullname):
            raise forms.ValidationError("Only alphabetic characters and space are allowed.")
        return fullname

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 8:
            raise forms.ValidationError("Minimum 8 characters.")
        if not re.match(r'^[A-Za-z0-9_@-]+$', username):
            raise forms.ValidationError("Only alphabetic, numeric, and symbols -, @, or _ are allowed.")
        if User.objects.filter(username=username).exists() == True:
            raise forms.ValidationError("Username is already taken.")
        return username

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 12:
            raise forms.ValidationError("Minimum 12 characters.")
        if not re.search(r'[A-Z]', password1):
            raise forms.ValidationError("Capital letter is missing.")
        if not re.search(r'\d', password1):
            raise forms.ValidationError("Numeric character is missing.")
        if not re.search(r'[_@-]', password1):
            raise forms.ValidationError("Symbol -, @, _ is missing.")
        if not re.match(r'^[A-Za-z0-9_@-]+$', password1):
            raise forms.ValidationError("Only symbols -, @, and _ are allowed.")
        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        return password2