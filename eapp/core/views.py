from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'core/index.html')

def login(request):
    return render(request,'core/login.html')

def wlist(request):
    return render(request,'core/product_list.html')

def cart(request):
    return render(request,'core/cart.html')

def checkout(request):
    return render(request,'core/checkout.html')

def catagory(request):
    return render(request,'core/catagori.html')