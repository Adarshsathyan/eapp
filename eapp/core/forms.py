from django import forms
from .models import Checkout, Products



class SearchForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['product_name']