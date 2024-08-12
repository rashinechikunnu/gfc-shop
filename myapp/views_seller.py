from django.shortcuts import render,redirect
from .forms import LoginForms,SellerForms





def seller_home_page(request):
    return render(request,'seller/seller_home.html')



# customer account creation

def seller_account_creation(request):
    
    l_form = LoginForms()
    s_form = SellerForms()
    
    if request.method == "POST":
        
        l_form = LoginForms(request.POST)
        
        s_form = SellerForms(request.POST)
        
        if l_form.is_valid() and s_form.is_valid():
            a = l_form.save(commit=False)
            a.is_seller = True
            a.save()
            user1= s_form.save(commit=False)
            user1.user=a
            user1.save()
        
            return redirect('seller_home')
        
    return render(request,"seller/create_account.html",{'l_form':l_form,'s_form':s_form})
