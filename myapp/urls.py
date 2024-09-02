from django.urls import path
from . import views,views_customer,views_seller,views_admin
urlpatterns = [

    # with out login
    path('',views.home,name='home'),
    path('login',views.log_in,name='login'),
    

    # main page men product area
    # men_shoe
    path('men_shoe',views.mens_shoe,name='shoe'),
    # men_cloth
    path('men_cloth',views.mens_cloth,name='cloth'),
    # men_accessories
    path('men_accessories',views.mens_accessories,name='accessories'),


    # main page women product area
    # women_shoe
    path('women_shoe',views.women_shoe,name='women_shoe'),
    # women_cloth
    path('women_cloth',views.women_cloth,name='women_cloth'),
    # women_accessories
    path('women_accessories',views.women_accessories,name='women_accessories'),



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
    path('customer_home',views_customer.home_page,name='customer_home'),
    # account creation
    path('customer_registration',views_customer.customer_account_creation,name='customer_registration'),
    # logout
    path('log_out',views_customer.log_out,name='log_out'),
    # add to cart
    path('add_to_cart/<pk>',views_customer.add_cart,name="add_to_cart"),
    # cart view
    path('views_cart',views_customer.view_cart,name="views_cart"),
    # remove cart
    path('remove_carts/<pk>',views_customer.remove_cart,name='remove_carts'),
    # payment area
    path('product_payment/<pk>',views_customer.payment,name='product_payment'),




    # Seller area
    path('seller_home',views_seller.seller_home_page,name='seller_home'),
    # create account
    path('seller_registration',views_seller.seller_account_creation,name='seller_registration'),
    # add product
    path('add_product',views_seller.add_product,name='add_product'),
    # view product
    path('s_view_product',views_seller.product_view,name='s_view_product'),
    # product full details
    path("detail_product<pk>",views.product_details,name="detail_product"),
    # edit product
    path("edit_product/<pk>",views_seller.edit_product,name="edit_product"),
    # delete product 
    path("delete_product/<pk>",views_seller.delete_product,name="delete_product")


]
