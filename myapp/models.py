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
    


class product(models.Model):
    sellers=models.ForeignKey(seller,on_delete=models.CASCADE)
    brand = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="media/")
    quantity = models.IntegerField(default=1)
    category =(
                    (1,"shoe"),
                    (2,"cloth"),
                    (3,"accessories")
                                 
    )
    product_category = models.IntegerField(choices=category,null=True,blank=True)
    sex_category = (
                      
                      (1,"men"),
                      (2,"women"),
                      (3,"unisex"),
    )
    sex = models.IntegerField(choices=sex_category,null=True,blank=True)
    specification = models.TextField()

    price = models.CharField(max_length=6)


    def __str__(self):
        return self.name
    

class add_to_cart(models.Model):
    customers = models.ForeignKey(Customer,on_delete=models.CASCADE)
    products= models.ForeignKey(product,on_delete=models.CASCADE)
    payment_status=models.IntegerField(default=0)

class payment_product(models.Model):
    # payment session
    add_to_cart_id = models.ForeignKey(add_to_cart,on_delete=models.CASCADE)
    card_holder_name = models.CharField(max_length=50)
    card_number = models.CharField(max_length=16)
    card_expiration =models.CharField(max_length=7)
    card_cvv = models.CharField(max_length=7)
    
    # delivery address
    order_address = models.CharField(max_length=200)
    phone_number=models.CharField(max_length=10)
    product_quantity=models.IntegerField()


# customer feedback
class Feedback(models.Model):
    user = models.ForeignKey(Customer,on_delete=models.DO_NOTHING)
    product_feedback = models.ForeignKey(product,on_delete=models.CASCADE)
    text_me = models.TextField()
    date = models.DateField(auto_now_add=True)
    replay = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.text_me