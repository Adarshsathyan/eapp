from django import forms
from .models import Checkout, Products


#class shippingForm(forms.ModelForm):
    #class Meta:
       # model = Checkout
       # fields =['name', 'email', 'phonenumber', 'address', 'state', 'district', 'zipcode']



class SearchForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['product_name']