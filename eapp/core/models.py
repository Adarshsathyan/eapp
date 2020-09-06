from django.db import models

# Create your models here.
class Products(models.Model):
    image = models.ImageField(upload_to='static/assets/img')
    product_name= models.CharField(max_length=200)
    price = models.IntegerField(max_length=50)