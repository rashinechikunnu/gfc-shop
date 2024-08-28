from django.shortcuts import render,redirect
from .forms import LoginForms,CustomerForms
from .models import product

# customer account creation

def home_page(request):
    return render(request,"customer/customer_home.html")

def customer_account_creation(request):
    
    l_form = LoginForms()
    c_form = CustomerForms()
    
    if request.method == "POST":
        
        l_form = LoginForms(request.POST)
        
        c_form = CustomerForms(request.POST)
        
        if l_form.is_valid() and c_form.is_valid():
            a = l_form.save(commit=False)
            a.is_customer = True
            a.save()
            user1= c_form.save(commit=False)
            user1.user=a
            user1.save()
        
            return redirect('customer_home')
        
    return render(request,"customer/create_account.html",{'l_form':l_form,'c_form':c_form})

