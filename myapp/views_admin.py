from django.shortcuts import render,redirect
from .models import seller,Customer,product



def home_page(request):
    return render(request,'admin/home_page.html')



# request seller
def seller_request(request):
    s_list = seller.objects.filter(status = 0)
    return render(request,"admin/seller_request.html",{"s_list":s_list})


# approval sellers 
def seller_approve(request,pk):
    sellers = seller.objects.get(pk=pk)
    sellers.status = 1
    sellers.save()
    return redirect('seller_request')

# reject sellers
def seller_reject(request,pk):
    sellers = seller.objects.get(pk=pk)
    sellers.status=2 
    sellers.save()
    return redirect('seller_request')

# approval seller lists
def approve_seller_list(request):
    seller_approved = seller.objects.filter(status = 1)
    return render(request,"admin/approve_sellers_list.html",{"seller_approved":seller_approved})

# reject seller list
def reject_seller_list(request):
    reject_seller = seller.objects.filter(status=2)
    return render(request,"admin/reject_sellers_list.html",{"reject_seller":reject_seller})

# customer list
def customer_list(request):
    customers_list = Customer.objects.all()
    return render(request,"admin/customer_list.html",{"customers_list":customers_list})


# seller product list
def seller_product_list(request,pk):

    view_product = product.objects.filter(sellers=pk)
    print(view_product)
    
    return render(request,"admin/seller_product_list.html",{"view_product":view_product})

