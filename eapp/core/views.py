from django.http import HttpResponse
from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    product = Products.objects.all()
    return render(request,'core/index.html',{'product':product})

def login(request):
    return render(request,'core/login.html')

def wlist(request):
    return render(request,'core/product_list.html')

def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.cart_set.all()
    else:

        items = []
        order ={' get_cart_total':0 , 'get_cart_items':0}
    return render(request,'core/cart.html',{'items':items,'order':order})

def checkout(request):
    return render(request,'core/checkout.html')

def catagory(request):
    return render(request,'core/catagori.html')

def about(request):
    return render(request,'core/about.html')

def confirmation(request):
    return render(request,'core/confirmation.html')

def contact(request):
    return render(request,'core/contact.html')