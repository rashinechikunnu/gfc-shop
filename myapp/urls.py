from django.urls import path
from . import views,views_customer,views_seller,views_admin
urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.log_in,name='login'),


    # Admin Area

    path('admin_home',views_admin.home_page,name="admin_home"),
    # seller list
    path('seller_list',views_admin.seller_list,name="seller_list"),
    # seller request
    path('request_seller/<pk>',views_admin.seller_approve,name='request_seller'),




    # Customer area
    path('customer_home',views_customer.home_page,name='customer_home'),
    path('customer_registration',views_customer.customer_account_creation,name='customer_registration'),
    path('log_out',views.log_out,name='log_out'),


    # Seller area
    path('seller_home',views_seller.seller_home_page,name='seller_home'),
    path('seller_registration',views_seller.seller_account_creation,name='seller_registration'),
    


]
