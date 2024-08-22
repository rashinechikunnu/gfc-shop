from django.contrib import admin
from .models import Login,Customer,seller,product

# Register your models here.

admin.site.register(Login),
admin.site.register(Customer),
admin.site.register(seller),
admin.site.register(product),
