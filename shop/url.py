from django.contrib import admin
from django.urls import path
from shop.views import  ShopProductListView, ShopCartView, ShopCheckoutView,ShopUpdateItem
from . import views

urlpatterns = [
    # path('restaurants/',RestaurantListView , name='restaurants-json-view'),
    path('cart/',views.ShopCartView, name='cart-view'),
    path('update_item/',views.ShopUpdateItem, name='update-cart-view'),
    path('checkout/',views.ShopCheckoutView , name='checkout-view'),
    path('products/<shop_id>/',ShopProductListView.as_view() , name='products-view'),

]

