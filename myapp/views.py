from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

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
                else:
                    messages.info(request,'wait for admin approval')
                
       
        else:
            messages.info(request,'invalid username and password')
    return render(request,"login.html")


# logout

def log_out(request):
    logout(request)
    return redirect('home')
  