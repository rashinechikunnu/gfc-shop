from django.urls import path
from . import views,views_customer,views_seller
urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.log_in,name='login'),



    # Customer area
    path('customer_registration',views_customer.customer_account_creation,name='customer_registration'),


    # Seller area
    path('seller_registration',views_seller.seller_account_creation,name='seller_registration'),
    


]
