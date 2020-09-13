from django.http import HttpResponse
from django.shortcuts import render
from .models import Products,Cart
# Create your views here.
def index(request):
    product = Products.objects.all()
    return render(request,'core/index.html',{'product':product})

def login(request):
    return render(request,'core/login.html')

def wlist(request):
    return render(request,'core/product_list.html')

def cart(request):
    items = Cart.objects.all()
    product = Products.objects.all()
    return render(request,'core/cart.html',{'items':items,'product':product})

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