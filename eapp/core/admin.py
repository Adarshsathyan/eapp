from django.contrib import admin
from .models import *
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','price','image')
admin.site.register(Products,ProductAdmin)

class CartAdmin(admin.ModelAdmin):

    list_display = ('id','order','quantity')
admin.site.register(Cart,CartAdmin)

class CustomerAdmin(admin.ModelAdmin):

    list_display = ('user','name','email')
admin.site.register(Customer,CustomerAdmin)

class OrderAdmin(admin.ModelAdmin):

    list_display = ('customer','complete','transaction_id')
admin.site.register(Order,OrderAdmin)

class CheckoutAdmin(admin.ModelAdmin):

    list_display = ('customer','address','city','state','zipcode')
admin.site.register(Checkout,CheckoutAdmin)