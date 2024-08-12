from django.shortcuts import render,redirect
from .models import seller,Customer



def home_page(request):
    return render(request,'admin/home_page.html')



# seller list
def seller_list(request):
    s_list = seller.objects.filter(status = 0)
    return render(request,"admin/sellers_list.html",{"s_list":s_list})


# approval sellers 
def seller_approve(request,pk):
    sellers = seller.objects.get(pk=pk)
    sellers.status = 1
    sellers.save()
    
    return render(request,'admin/home_page.html',{"sellers":sellers})