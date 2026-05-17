from django.contrib import admin
from .models import Type, Flavour

# Register your models here.

class TypeAdmin(admin.ModelAdmin):
    list_display = ("id","name","description", "price","image")

class FlavourAdmin(admin.ModelAdmin):
    list_display = ("id","name","description","image")

admin.site.register(Type, TypeAdmin)
admin.site.register(Flavour, FlavourAdmin)


# Creating order with no account
from .models import Customer, Order, Ordered_Donuts

class CustomerAdmin(admin.ModelAdmin):
    list_display = ("id","firstName","lastName","address", "phoneNo","email")

class Ordered_DonutsAdmin(admin.ModelAdmin):
    list_display = ("id","orderID","typeID","flavorID","quantity")

class OrderAdmin(admin.ModelAdmin):
    list_display = ("id","custID","date")

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Ordered_Donuts, Ordered_DonutsAdmin)
