from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('wlist/',views.wlist,name='wlist'),
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('catogary/', views.catagory, name='catagory'),
    path('about/', views.about, name='about'),
    path('confirmation', views.confirmation, name='confirmation'),
    path('contact/', views.contact, name='contact'),
    path('updateitem/',views.UpdateItem,name='updateitem'),
    path('process_order/',views.processOrder,name='process_order'),

]