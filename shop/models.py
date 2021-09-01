from django.db import models
from home.models import Account

# Create your models here.
class Status( models.IntegerChoices ):
    ACTIVE = 1, 'Active'
    NOT_ACTIVE = 0, 'Not Active'

class DeliveryDuration( models.IntegerChoices ):
    DD_1 = 10, '10 Minutes'
    DD_2 = 20, '20 Minutes'
    DD_3 = 30, '30 Minutes'
    DD_4 = 40, '40 Minutes'
    DD_5 = 50, '50 Minutes'
    DD_6 = 60, '1 Hour'

class Restaurant( models.Model ):
    restaurant_name = models.CharField( max_length=100 , null= True)
    restaurant_address = models.CharField( max_length=200, null= True )
    restaurant_delivery_duration = models.IntegerField( default=DeliveryDuration.DD_2, choices=DeliveryDuration.choices )
    restaurant_status = models.IntegerField( default=Status.ACTIVE, choices=Status.choices )
    restaurant_opening_time = models.TimeField()
    restaurant_closing_time= models.TimeField()
    restaurant_logo = models.ImageField( upload_to='images/' ,default='images/default_logo.jpg' )

    def __str__( self ):
        return self.restaurant_name

class ProductCategory( models.Model ):
    cat_title = models.CharField( max_length=50 , null= True )
    cat_desc = models.TextField( null= True )
    cat_status = models.IntegerField( default=Status.ACTIVE, choices=Status.choices )
    
    def __str__( self ):
        return self.cat_title

class MediaGallery( models.Model ):
    media_title = models.CharField( max_length=50, null= True )
    image1 = models.ImageField( upload_to='images' )
    image2 = models.ImageField( upload_to='images' )
    image3 = models.ImageField( upload_to='images' )

    def __str__( self ):
        return self.media_title

class Product( models.Model ):
    product_title = models.CharField( max_length=100, null= True )
    product_desc = models.TextField( null= True )
    product_price = models.DecimalField( max_digits=6, decimal_places=2 )
    product_status = models.IntegerField( default=Status.ACTIVE, choices=Status.choices )
    product_cat = models.ForeignKey( ProductCategory, on_delete=models.SET_NULL, null=True, blank=True)
    restaurant = models.ForeignKey( Restaurant, on_delete=models.SET_NULL, null=True, blank=True )
    product_media = models.ForeignKey( MediaGallery, on_delete=models.SET_NULL, null=True, blank=True )
    
    def __str__( self ):
        return self.product_title

class Order( models.Model ):
    customer = models.ForeignKey( Account, on_delete=models.SET_NULL, null=True, blank=True )
    date_ordered = models.DateTimeField( auto_now_add=True )
    complete = models.BooleanField( default=False )
    transaction_id = models.CharField( max_length=100, null=True )

    def __str__( self ):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

class OrderItem( models.Model ):
    product = models.ForeignKey( Product, on_delete=models.SET_NULL, null=True, blank=True )
    order = models.ForeignKey( Order, on_delete=models.SET_NULL, null=True, blank=True )
    quantity = models.IntegerField( default=0, null=True, blank=True )
    date_added = models.DateTimeField( auto_now_add=True )
    
    @property
    def get_total( self ):
        total = self.product.product_price * self.quantity
        return total

class ShippingAddress( models.Model ):

    customer = models.ForeignKey( Account, on_delete=models.SET_NULL, null=True, blank=True )
    order = models.ForeignKey( Order, on_delete=models.SET_NULL, null=True, blank=True )
    address = models.CharField( max_length=200, null= True )
    city = models.CharField( max_length=200, null= True )
    state = models.CharField( max_length=200, null= True )
    zipcode = models.CharField( max_length=200, null= True )
    date_added = models.DateTimeField( auto_now_add=True )

    def __str__( self ):
        return self.address
