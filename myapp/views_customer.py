from django.shortcuts import render,redirect
from .forms import LoginForms,CustomerForms,paymentForm
from .models import product,add_to_cart,Customer,payment_product
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


# customer add to cart
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

# customer view CART
def view_cart(request):
    user_get= request.user
    user_customer =Customer.objects.get(user=user_get)
    cart_views = add_to_cart.objects.filter(customers=user_customer)
    print(cart_views)

    return render(request,"customer/view_cart.html",{"cart_views":cart_views})



# remove product in cart
def remove_cart(request,pk):
    product_remove=add_to_cart.objects.get(pk=pk)
    product_remove.delete()
    cart_views = add_to_cart.objects.all()
    return render(request,"customer/view_cart.html",{"cart_views":cart_views})


# payment

def payment(request,pk):
    product_payment = add_to_cart.objects.get(pk=pk)
    print(product_payment)
    card_name = request.POST.get("user_card_name")
    print(card_name)
    card_number = request.POST.get("user_card_number")
    print(card_number)
    card_expiration = request.POST.get("user_card_expiration")  
    print(card_expiration)
    card_cvv = request.POST.get("user_cvv" )
    print(card_cvv)
    


    if request.method == 'POST':
        
        pay=payment_product()
        pay.add_to_cart_id = product_payment
        print(pay.add_to_cart_id)
        pay.card_holder_name = card_name
        print(pay.card_holder_name)
        pay.card_number = card_number
        pay.card_expiration=card_expiration
        pay.card_cvv= card_cvv
        pay.save()
        
        product_payment.payment_status = 1
        product_payment.save()
        return redirect('customer_home')
    return render(request,"customer/payment.html")
            

 


# logout

def log_out(request):
    logout(request)
    return redirect('home')
