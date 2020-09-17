from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
# Create your views here.
def index(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.cart_set.all()
        cartItem = order.get_cart_items
    else:
        items = []
        order ={'get_cart_total':0 , 'get_cart_items':0}
        cartItem = order['get_cart_items']
    product = Products.objects.all()
    return render(request,'core/index.html',{'product':product, 'items': items ,'cartItem': cartItem})

def login(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.cart_set.all()
        cartItem = order.get_cart_items
    else:
        items = []
        order ={'get_cart_total':0 , 'get_cart_items':0}
        cartItem = order['get_cart_items']
    return render(request,'core/login.html',{'items': items ,'cartItem': cartItem})

def wlist(request):
    return render(request,'core/product_list.html')

def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.cart_set.all()
        cartItem = order.get_cart_items
    else:

        items = []
        order ={' get_cart_total':0 , 'get_cart_items':0}
        cartItem = order['get_cart_items']
    return render(request,'core/cart.html',{'items':items,'order':order,'cartItem': cartItem})

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.cart_set.all()
        cartItem = order.get_cart_items
    else:

        items = []
        order = {' get_cart_total': 0, 'get_cart_items': 0}
        cartItem = order['get_cart_items']
    context = {'items':items,'order':order,'cartItem': cartItem}
    return render(request,'core/checkout.html',context)

def catagory(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.cart_set.all()
        cartItem = order.get_cart_items
    else:

        items = []
        order = {' get_cart_total': 0, 'get_cart_items': 0}
        cartItem = order['get_cart_items']
    context = {'items':items,'order':order,'cartItem': cartItem}
    return render(request,'core/catagori.html',context)

def about(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.cart_set.all()
        cartItem = order.get_cart_items
    else:

        items = []
        order = {' get_cart_total': 0, 'get_cart_items': 0}
        cartItem = order['get_cart_items']
    context = {'items':items,'order':order,'cartItem': cartItem}
    return render(request,'core/about.html',context)

def confirmation(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.cart_set.all()
        cartItem = order.get_cart_items
    else:

        items = []
        order = {' get_cart_total': 0, 'get_cart_items': 0}
        cartItem = order['get_cart_items']
    context = {'items':items,'order':order,'cartItem': cartItem}
    return render(request,'core/confirmation.html',context)

def contact(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.cart_set.all()
        cartItem = order.get_cart_items
    else:

        items = []
        order = {' get_cart_total': 0, 'get_cart_items': 0}
        cartItem = order['get_cart_items']
    context = {'items':items,'order':order,'cartItem': cartItem}
    return render(request,'core/contact.html',context)

def UpdateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:',action)
    print('ProductId:', productId)


    customer = request.user.customer
    product = Products.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = Cart.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse('item was added', safe=False)