from django.shortcuts import render,redirect
from .forms import LoginForms,CustomerForms
from .models import product,add_to_cart,Customer
from django.contrib.auth import authenticate,login,logout

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


# add to cart
def add_cart(request,pk):
        get_user=request.user
        print(get_user)
        if not get_user.is_authenticated:
             return redirect("login")
        else:
            data=Customer.objects.get(user=get_user)
            product_id = product.objects.get(pk=pk)
            cart_item= add_to_cart.objects.create(products=product_id, customers=data)
            cart_item.save()
            return redirect('views_cart')
# view CART
def view_cart(request):
    user_get= request.user
    user_customer =Customer.objects.get(user=user_get)
    cart_views = add_to_cart.objects.filter(customers=user_customer)

    return render(request,"customer/view_cart.html",{"cart_views":cart_views})



# logout

def log_out(request):
    logout(request)
    return redirect('home')
