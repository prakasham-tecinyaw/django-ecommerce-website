from .models import Order, Restaurant, Product, MediaGallery


def update_product_count(res_id, *args, **kwargs):
    #query product count

    res = Product.objects.filter(restaurant=res_id).count()

    return res

def get_product_media_gallery(product_id, *args, **kwargs):

    media_query = MediaGallery.objects.filter(product=product_id)

    for media in media_query:
        media_list = {
            'image1': media.image1,
            'image2': media.image2,
            'image3': media.image3,
        }

    return media_list

def home_page_shop_list():

    shops = Restaurant.objects.filter(restaurant_status='1')
    shops_obj = []
    # total_product_count =[]

    for shop in shops:
        p_count = update_product_count(shop.id)
        data = {
            'id': shop.id,
            'restaurant_name': shop.restaurant_name,
            'restaurant_address': shop.restaurant_address,
            'restaurant_opening_time': shop.restaurant_opening_time,
            'restaurant_closing_time': shop.restaurant_closing_time,
            'restaurant_logo': shop.restaurant_logo,
            'restaurant_product_count': p_count,
        }
        shops_obj.append(data)
        # total_product_count.append( p_count )

    return shops_obj

def shopping_cart_items(items):

    total_obj = []
    for item in items:
        product_media = get_product_media_gallery(
            item.product.product_media.id)
        data = {
            'id': item.product.id,
            'product_title': item.product.product_title,
            'product_qty': item.quantity,
            'product_price': item.product.product_price,
            'product_media': product_media['image1'],
            'get_total':item.get_total
        }
        total_obj.append(data)

    return total_obj

def total_cart_quantity( customer ):

    order, created = Order.objects.get_or_create( customer = customer, complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items

    return cartItems