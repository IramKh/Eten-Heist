from django.db.models import fields
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CustomerUpdateForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class Product_Detail_form(ModelForm):
    class Meta:
        model = Our_Product
        fields = '__all__'

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
