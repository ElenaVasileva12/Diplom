from django.contrib import admin
from django.urls import path
from . import views
from .temporary_products.auth import  auth_temporary_products


urlpatterns = [
    path('', views.Index.as_view(), name='homepage'),
    path('store', views.store , name='store'),

    path('signup', views.Signup.as_view(), name='signup'),
    path('login', views.Login.as_view(), name='login'),
    path('logout', views.logout , name='logout'),
    path('cart', auth_temporary_products(views.Cart.as_view()) , name='cart'),
    path('check-out', views.CheckOut.as_view() , name='checkout'),
    path('orders', auth_temporary_products(views.OrderView.as_view()), name='orders'),

]


