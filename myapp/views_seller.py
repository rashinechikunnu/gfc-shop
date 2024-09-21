from django.shortcuts import render,redirect
from .forms import LoginForms,SellerForms,prodctForms
from .models import seller,product,payment_product
from django.contrib.auth.decorators import login_required



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


# seller Home
@login_required(login_url='login')
def seller_home_page(request):
    return render(request,'seller/seller_home.html')



# add products
@login_required(login_url='login')
def add_product(request):
 
    getseller = request.user
    data = seller.objects.get(user = getseller)

    if request.method == "POST":
        add_product_form = prodctForms(request.POST, request.FILES)
        
        if add_product_form.is_valid():

            obj = add_product_form.save(commit = False)
            obj.sellers = data
            obj.save()
            return redirect('s_view_product')
        
    else:
        add_product_form=prodctForms()

    return render(request,'seller/add_product.html',{'add_prodct_form':add_product_form})



# view products
@login_required(login_url='login')
def product_view(request):
    get_uesr = request.user
    data = seller.objects.get(user=get_uesr)

    view_product = product.objects.filter(sellers=data)
    return render(request,'seller/views_product.html',{'view_product':view_product})



# edit product
@login_required(login_url='login')
def edit_product(request,pk):

    edt = product.objects.get(pk=pk)
    if request.method == "POST":
        product_edt = prodctForms(request.POST,request.FILES, instance=edt)
        if product_edt.is_valid():
            edt.save()
            return redirect('s_view_product')
    else:
        product_edt = prodctForms(instance=edt)
        
    return render(request,"seller/product_edit.html",{"product_edt":product_edt})



# delete product
@login_required(login_url='login')
def delete_product(request,pk):
    detl = product.objects.get(pk=pk)
    detl.delete()
    return redirect("s_view_product")



# order product
@login_required(login_url='login')
def product_order(request):
    get_seller = request.user
    seller_data = seller.objects.get(user=get_seller)
    ordering_product= payment_product.objects.filter(add_to_cart_id__payment_status=1, add_to_cart_id__products__sellers = seller_data)
    print(ordering_product)
    return render(request,"seller/order_product.html",{"ordering_product":ordering_product})

