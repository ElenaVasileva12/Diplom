from django.contrib import admin
from .models import Category, Product,Customer,Order


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']



class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price',  'category']
 
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order)

