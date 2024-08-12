from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

# LOGIN

class Login(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_seller = models.BooleanField(default = False)
    

# customer models

class Customer(models.Model):
    user = models.ForeignKey(Login,on_delete= models.CASCADE)
    Name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    email=models.EmailField()
    address = models.CharField(max_length=200)


    def __str__(self):
        return self.Name
    
# seller models

class seller(models.Model):
    user = models.ForeignKey(Login,on_delete= models.CASCADE)
    Name=models.CharField(max_length=100)
    contact=models.CharField(max_length=10)
    email = models.EmailField()
    shop_address = models.CharField(max_length=200)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.Name
    

