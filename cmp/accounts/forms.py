from django.forms import ModelForm, TextInput, EmailInput, PasswordInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Order

class OrderForm(ModelForm):
	class Meta:
		model = Order
		fields = '__all__'

class CreateUserForm(UserCreationForm):
	password1 = forms.CharField(label="Password",
		widget=forms.PasswordInput(
			attrs={'class':'form-control form-control-md', 'type':'password', 'align':'center'}))
	password2 = forms.CharField(label="Confirm password",
		widget=forms.PasswordInput(
			attrs={'class':'form-control form-control-md', 'type':'password', 'align':'center'}))

	class Meta:
		model = User
		fields = ['username', 'email']
		widgets = {
            'username': TextInput(attrs={
                'class': "form-control form-control-md"}),
            'email': EmailInput(attrs={
                'class': "form-control form-control-md"}),
        }

