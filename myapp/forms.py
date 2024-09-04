from django.contrib.auth.forms import UserCreationForm

from django import forms
from .models import Customer,Login,seller,product,payment_product,Feedback

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
        exclude = ("user","status")


# seller add product form

class prodctForms(forms.ModelForm):
    
    class Meta:
        model = product
        fields ="__all__"
        exclude = ("sellers",)


# payment forms
class paymentForm(forms.ModelForm):
    class Meta:
        model = payment_product
        fields ="__all__"
        exclude = ("add_to_cart_id",)



# feedback forms
class feedbackForms(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('text_me'),
