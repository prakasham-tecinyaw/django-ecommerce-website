from django.contrib import admin
from . import models
from shop.models import Product, Restaurant, MediaGallery, ProductCategory, Order, OrderItem, ShippingAddress
# Register your models here.

class AppAdminArea(admin.AdminSite):
    site_header ='OhMyFoot Admin'

# Admin Site
admin_site = AppAdminArea( name = 'AppAdmin' )

# shop Site
admin_site.register( models.Account )
admin_site.register( Product)
admin_site.register( Restaurant)
admin_site.register( MediaGallery)
admin_site.register( ProductCategory)
admin_site.register( Order)
admin_site.register( OrderItem)
admin_site.register( ShippingAddress)

