from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# Create your models here.
class Products(models.Model):
    image = models.ImageField(upload_to='static/assets/img', blank=True, null= True)
    product_name= models.CharField(max_length=200,blank=True)
    digital = models.BooleanField(default=False,null=True,blank=True)
    price = models.FloatField()

    def __str__(self):
        return self.product_name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):
        shipping = False
        orderitems = self.cart_set.all()
        for i in orderitems:
            if i.order.complete == False:
                shipping = True
        return shipping

    @property
    def get_cart_total(self):
        orderitems = self.cart_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.cart_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

    @property
    def tot(self):
        orderitems = self.cart_set.all()
        total = sum([item.get_total for item in orderitems])
        t = int(total+50)
        return t


class Cart(models.Model):
    product = models.ForeignKey(Products,on_delete=models.SET_NULL,null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.quantity * self.product.price
        return total

    def __str__(self):
        return str(self.id)
    

class Checkout(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL,null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=True)
    district = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    phonenumber = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)



    def __str__(self):
	    return self.address


class Contact(models.Model):
    message = models.TextField(max_length=1000)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)