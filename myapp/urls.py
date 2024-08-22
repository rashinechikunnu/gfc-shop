from django.urls import path
from . import views,views_customer,views_seller,views_admin
urlpatterns = [
   
    path('',views.home,name='home'),
    path('login',views.log_in,name='login'),
    path('shoe',views.shoe,name='shoe'),



    # Admin Area
    path('admin_home',views_admin.home_page,name="admin_home"),
    # seller request
    path('seller_request',views_admin.seller_request,name="seller_request"),
    # seller approval request
    path('approval_seller/<pk>',views_admin.seller_approve,name='approval_seller'),
    # seller reject
    path('reject_seller/<pk>',views_admin.seller_reject,name="reject_seller"),
    # approved sellers list
    path('approvaed_sellers_list',views_admin.approve_seller_list,name="approved_sellers_list"),
    # reject sellers list
    path('reject_sellers_list',views_admin.reject_seller_list,name="reject_sellers_list"),
    # customers list
    path('customers_list',views_admin.customer_list,name="customers_list"),
    # seller_product view
    path('product_view/<pk>',views_admin.seller_product_list,name="product_view"),






    # Customer area

    # home
    path('customer_home',views_customer.home_page,name='customer_home'),
    # account creation
    path('customer_registration',views_customer.customer_account_creation,name='customer_registration'),
    # logout
    path('log_out',views.log_out,name='log_out'),
    # show product
    path('show_product',views_customer.product_show,name='show_product'),





    # Seller area

    # home page
    path('seller_home',views_seller.seller_home_page,name='seller_home'),
    # create account
    path('seller_registration',views_seller.seller_account_creation,name='seller_registration'),
    # add product
    path('add_product',views_seller.add_product,name='add_product'),
    # view product
    path('view_product',views_seller.product_view,name='view_product'),

    


]
