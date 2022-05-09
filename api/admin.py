from django.contrib import admin
from .models import Product, Pay, Order, ItemOrder, Record, Category, Stock


# Register your models here.

class AdminProduct(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Product, AdminProduct)


class AdminOrder(admin.ModelAdmin):
    list_display = ('id', 'date', 'total',)


admin.site.register(Order, AdminOrder)


class AdminItemOrder(admin.ModelAdmin):
    list_display = ('id', 'name', 'quantity')


admin.site.register(ItemOrder, AdminItemOrder)


class AdminRecord(admin.ModelAdmin):
    list_display = ('id', 'creation_date')


admin.site.register(Record, AdminRecord)
