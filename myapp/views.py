from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from . models import product
from myapp.filter import PlaceFilter
from myapp.models import seller
from django.core.paginator import Paginator


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



# mens area

# all men shoe view  customer
def mens_shoe(request):

    shoe_list = product.objects.filter(product_category=1,sex=3)
    list_shoe = product.objects.filter(product_category=1,sex=1)
    
    combined_shoes = shoe_list | list_shoe
   
    placeFilter = PlaceFilter(request.GET, queryset=combined_shoes)
    data = placeFilter.qs

    paginator = Paginator(data,3)  
    page_number = request.GET.get('page')  
    page_obj = paginator.get_page(page_number)  

    return render(request,"all_men_shoe_list.html",{"combined_shoes":page_obj, 'placeFilter':placeFilter})


# all men cloth view customer
def mens_cloth(request):

    cloth_list = product.objects.filter(product_category=2,sex=1)
    list_cloth = product.objects.filter(product_category=2,sex=3)

    combined_cloth = cloth_list | list_cloth

    placeFilter = PlaceFilter(request.GET, queryset=combined_cloth)
    data = placeFilter.qs

    paginator = Paginator(data,3)  
    page_number = request.GET.get('page')  
    page_obj = paginator.get_page(page_number)
    
    return render(request,"all_men_cloth_list.html",{"combined_cloth":page_obj, "placeFilter":placeFilter})



# all men accessories view  customer
def mens_accessories(request):

    accessories_list = product.objects.filter(product_category=3,sex=1)
    list_accessories = product.objects.filter(product_category=3,sex=3)

    combined_accessories = accessories_list | list_accessories

    placeFilter = PlaceFilter(request.GET, queryset=combined_accessories)
    data = placeFilter.qs

    paginator = Paginator(data,3)  
    page_number = request.GET.get('page')  
    page_obj = paginator.get_page(page_number)

    return render(request,"all_men_accessories_list.html",{"combined_accessories":page_obj, "placeFilter":placeFilter})




# womens area


# all women shoe view  customer
def women_shoe(request):

    shoe_list = product.objects.filter(product_category=1,sex=2)
    list_shoe = product.objects.filter(product_category=1,sex=3)
    
    combined_shoes = shoe_list | list_shoe

    placeFilter = PlaceFilter(request.GET, queryset=combined_shoes)
    data = placeFilter.qs

    paginator = Paginator(data,3)  
    page_number = request.GET.get('page')  
    page_obj = paginator.get_page(page_number)

    return render(request,"all_men_shoe_list.html",{"combined_shoes":page_obj, "placeFilter":placeFilter})



# all women cloth view customer
def women_cloth(request):

    cloth_list = product.objects.filter(product_category=2,sex=2)
    list_cloth = product.objects.filter(product_category=2,sex=3)

    combined_cloth = cloth_list | list_cloth

    placeFilter = PlaceFilter(request.GET, queryset=combined_cloth)
    data = placeFilter.qs

    paginator = Paginator(data,3)  
    page_number = request.GET.get('page')  
    page_obj = paginator.get_page(page_number)

    return render(request,"all_men_cloth_list.html",{"combined_cloth":page_obj, "placeFilter":placeFilter})



# all women accessories view  customer
def women_accessories(request):

    accessories_list = product.objects.filter(product_category=3,sex=2)
    list_accessories = product.objects.filter(product_category=3,sex=3)

    combined_accessories = accessories_list | list_accessories

    placeFilter = PlaceFilter(request.GET, queryset=combined_accessories)
    data = placeFilter.qs

    paginator = Paginator(data,3)  
    page_number = request.GET.get('page')  
    page_obj = paginator.get_page(page_number)

    return render(request,"all_men_accessories_list.html",{"combined_accessories":page_obj, "placeFilter":placeFilter})




# product full details
def product_details(request,pk):
    details_product = product.objects.get(pk=pk)   
    return render(request,"product_full_details.html",{'details_product':details_product})



# logout
def log_out(request):
    logout(request)
    return redirect('home')





  