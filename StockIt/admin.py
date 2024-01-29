from django.contrib import admin
from .models import Product, Order
from django.contrib.auth.models import Group
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display=('Name','Category','Quantity')
    list_filter=['Category']

admin.site.site_header='StockIT Dashboard'
admin.site.register(Product,ProductAdmin)
admin.site.register(Order)
#admin.site.unregister(Group)

