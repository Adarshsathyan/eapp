from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse
import json
from .forms import ContactForm, CustomReg
import datetime
# Create your views here.
def index(request):
    product = Products.objects.all()
    if request.user.is_authenticated:
        Customer.objects.get_or_create(user=request.user)
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.cart_set.all()
        cartItem = order.get_cart_items
    else:
        items = []
        order ={'get_cart_total':0 , 'get_cart_items':0 ,'shipping':True}
        cartItem = order['get_cart_items']

    return render(request,'core/index.html',{'product':product, 'items': items ,'cartItem': cartItem})

def login(request):
    if request.user.is_authenticated:
        Customer.objects.get_or_create(user=request.user)
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.cart_set.all()
        cartItem = order.get_cart_items

    else:
        items = []
        order ={'get_cart_total':0 , 'get_cart_items':0}
        cartItem = order['get_cart_items']
    return render(request, 'registration/login.html', {'items': items, 'cartItem': cartItem})


def wlist(request):
    return render(request,'core/product_list.html')

@login_required
def cart(request):

    if request.user.is_authenticated:
        Customer.objects.get_or_create(user=request.user)
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
        Customer.objects.get_or_create(user=request.user)
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
        Customer.objects.get_or_create(user=request.user)
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
        Customer.objects.get_or_create(user=request.user)
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
        Customer.objects.get_or_create(user=request.user)
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
        Customer.objects.get_or_create(user=request.user)
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.cart_set.all()
        cartItem = order.get_cart_items

    else:

        items = []
        order = {' get_cart_total': 0, 'get_cart_items': 0}
        cartItem = order['get_cart_items']
    form = ContactForm()
    context = {'items':items,'order':order,'cartItem': cartItem,'form':form}
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

def processOrder(request):

    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == order.get_cart_total:
            order.complete = True
        order.save()
        Checkout.objects.create(
        customer=customer,
        order=order,
        address = data['shipping']['address'],
        phonenumber = data['shipping']['phnumber'],
        district = data['shipping']['district'],
        state = data['shipping']['state'],
        zipcode = data['shipping']['zip'],
        )

    else:
        print("user not logge in")
    return JsonResponse('payment completed', safe=False)
def connect(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
            return redirect('index')

def register(request):
    form = CustomReg()
    if request.method == 'POST':
        form = CustomReg(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request,'registration/register.html', {'form':form})