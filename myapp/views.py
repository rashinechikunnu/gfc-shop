from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from . models import product

from myapp.models import seller

# Create your views here.

def home(request):

    return render(request,"home.html")

# login 

def log_in(request):

    if request.method == "POST":
        user_name = request.POST.get('user_name')
        print(user_name)
        user_password = request.POST.get('user_password')
        print(user_password)
        
        user_click=authenticate(request,username=user_name,password=user_password)
        print(user_click)

        if user_click is not None:
            login(request,user_click)
        
            if user_click.is_staff:
                return redirect('admin_home')
            
            elif user_click.is_customer:
                return redirect('customer_home')
            
           
            elif user_click.is_seller:
                stat = seller.objects.get(user = user_click)
                if stat.status == 1 :

                    return redirect('seller_home')
                elif stat.status == 2:
                    messages.info(request,'admin rejected your account')
                else:
                    messages.info(request,"waiting for admin approval")
                
       
        else:
            messages.info(request,'invalid username and password')
    return render(request,"login.html")


# all shoe view with out login customer

def shoe(request):
    shoe_list = product.objects.filter(product_category=1)
    print(shoe_list)
    return render(request,"all_shoe_list.html",{"shoe_list":shoe_list})


# all cloth view with out login customer

def cloth(request):
    cloth_list = product.objects.filter(product_category=2)
    print(cloth_list)
    return render(request,"all_cloth_list.html",{"cloth_list":cloth_list})


# all accessories view with out login customer
def accessories(request):
    accessories_list = product.objects.filter(product_category=3)
    print(accessories_list)
    return render(request,"all_accessories_list.html",{"accessories_list":accessories_list})



# logout

def log_out(request):
    logout(request)
    return redirect('home')
  