from django.db import models

# Create your models here.

class Flavour(models.Model):
    name = models.CharField(max_length=255)

class Type(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(default=0.00)

class Customer(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

class Ordered_Donuts(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    flavor = models.ForeignKey(Flavour, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    quantity = models.IntegerField()