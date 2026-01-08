from django.contrib import admin
from .models import Category,Product,Order,OrderItem


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('category', 'name','slug', 'description', 'price')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user','status')

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order','product','price','quantity')
    