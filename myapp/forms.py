from django.contrib.auth.forms import UserCreationForm

from django import forms
from .models import Customer,Login,seller

# create a customer_data modelForm


# login form

class LoginForms(UserCreationForm):
    username=forms.CharField()
    password1=forms.CharField(label="password", widget=forms.PasswordInput(attrs={'placeholder': ''}))
    password2=forms.CharField(label="password",widget=forms.PasswordInput)
    class Meta:
        model = Login
        fields =('username',"password1","password2") 


# customer account creation form

class CustomerForms(forms.ModelForm):
    
    class Meta:
        model = Customer
        fields ="__all__"
        exclude = ("user",)


# seller account creation form

class SellerForms(forms.ModelForm):
    
    class Meta:
        model = seller
        fields ="__all__"
        exclude = ("user",)