from django.contrib import admin
from .models import Type, Flavour

# Register your models here.

class TypeAdmin(admin.ModelAdmin):
    list_display = ("id","name","description", "price","image")

class FlavourAdmin(admin.ModelAdmin):
    list_display = ("id","name","description","image")

admin.site.register(Type, TypeAdmin)
admin.site.register(Flavour, FlavourAdmin)