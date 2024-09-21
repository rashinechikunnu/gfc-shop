from django.shortcuts import render,redirect
from .models import seller,Customer,product,Feedback
from django.contrib.auth.decorators import login_required


# admin home page
@login_required(login_url='login')
def home_page(request):
    return render(request,'admin/home_page.html')



# request seller
@login_required(login_url='login')
def seller_request(request):
    s_list = seller.objects.filter(status = 0)
    return render(request,"admin/seller_request.html",{"s_list":s_list})


# approval sellers 
@login_required(login_url='login')
def seller_approve(request,pk):
    sellers = seller.objects.get(pk=pk)
    sellers.status = 1
    sellers.save()
    return redirect('seller_request')


# reject sellers
@login_required(login_url='login')
def seller_reject(request,pk):
    sellers = seller.objects.get(pk=pk)
    sellers.status=2 
    sellers.save()
    return redirect('seller_request')


# approval seller lists
@login_required(login_url='login')
def approve_seller_list(request):
    seller_approved = seller.objects.filter(status = 1)
    return render(request,"admin/approve_sellers_list.html",{"seller_approved":seller_approved})

# reject seller list
@login_required(login_url='login')
def reject_seller_list(request):
    reject_seller = seller.objects.filter(status=2)
    return render(request,"admin/reject_sellers_list.html",{"reject_seller":reject_seller})

# customer list
@login_required(login_url='login')
def customer_list(request):
    customers_list = Customer.objects.all()
    return render(request,"admin/customer_list.html",{"customers_list":customers_list})


# seller product list
@login_required(login_url='login')
def seller_product_list(request,pk):

    view_product = product.objects.filter(sellers=pk)
    print(view_product)
    
    return render(request,"admin/seller_product_list.html",{"view_product":view_product})


# feedback
@login_required(login_url='login')
def feedback_customer(request):
    
    feedback_customer_list = Feedback.objects.all() 
    
    return render(request,'admin/feedback_customer.html',{'fdb_customer':feedback_customer_list})


# replay feedback
@login_required(login_url='login')
def replay_cunstomer(request,pk):
    rply =Feedback.objects.get(pk=pk)
    if request.method == 'POST':
        rplyfrm = request.POST.get('replaaay')
        rply.replay=rplyfrm
        rply.save()
        return redirect('view_customer_feedback')
    
    return render(request,'admin/customer_replay.html',{'rply':rply})



