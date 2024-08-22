from django.shortcuts import render,redirect
from .forms import LoginForms,SellerForms,prodctForms
from .models import seller,product





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
        
            return redirect('login')
        
    return render(request,"seller/create_account.html",{'l_form':l_form,'s_form':s_form})


# add products
def add_product(request):
 
    getseller = request.user
    data = seller.objects.get(user = getseller)

    if request.method == "POST":
        add_product_form = prodctForms(request.POST, request.FILES)
        
        if add_product_form.is_valid():

            obj = add_product_form.save(commit = False)
            obj.sellers = data
            obj.save()
        
    else:
        add_product_form=prodctForms()

    return render(request,'seller/add_product.html',{'add_prodct_form':add_product_form})

# view products
def product_view(request):
    get_uesr = request.user
    data = seller.objects.get(user=get_uesr)

    view_product = product.objects.filter(sellers=data)
    return render(request,'seller/views_product.html',{'view_product':view_product})