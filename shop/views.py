from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem, Restaurant, Product

from django.views.generic import View, TemplateView
from django.db.models import Count

from shop.micro_views import update_product_count, get_product_media_gallery, shopping_cart_items, total_cart_quantity

import json
# Create your views here.

class ShopProductListView(TemplateView):
    def get(self, request, *args, **kwargs):

        context = {}
        shop_id = kwargs.get("shop_id")
        try:
            data_obj = list(
                Product.objects.all().filter(restaurant_id=shop_id))
        except:
            return HttpResponse("Something went wrong.")

        total_products = []

        for product in data_obj:

            media_list = get_product_media_gallery(product.id)

            data = {
                'id': product.id,
                'product_title': product.product_title,
                'product_desc': product.product_desc,
                'product_price': product.product_price,
                'product_cat': product.product_cat,
                'restaurant': product.restaurant,
                'media_1': media_list['image1'],
                'media_2': media_list['image2'],
                'media_3': media_list['image3'],
            }

            total_products.append(data)

            print(total_products)

        return render(request, 'all_product_page.html',
                      {'data': total_products})

def ShopUpdateItem( request, *args, **kwargs ):
    data = json.loads( request.body )
    product_id = data['productId']
    action = data['action']
    print(product_id,action)

    customer = request.user
    product = Product.objects.get(id=product_id)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)

    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
    
    return JsonResponse('Item was added ', safe=False)

@login_required(login_url='login')
def ShopCartView( request, *args, **kwargs):

    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
        result = shopping_cart_items(items)
        orders = total_cart_quantity(customer)

        context = {'items': result, 'order':order, 'get_cart_total':orders}
        return render(request, 'cart.html', context)
    else:
        return render(request, 'account/login.html')

@login_required(login_url='login')
def ShopCheckoutView(request, *args, **kwargs):
    
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
        result = shopping_cart_items(items)
        orders = total_cart_quantity(customer)

        context = {'items': result, 'order':order, 'get_cart_total':orders}
        return render( request, 'checkout.html', context )
    else:
        return render(request, 'account/login.html') 

    