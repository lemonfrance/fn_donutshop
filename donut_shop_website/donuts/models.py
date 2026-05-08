from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinLengthValidator

# Create your models here.

class Flavour(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(default='placeholder.png', blank=True)
    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField(default=0.00)
    image = models.ImageField(default='placeholder.png', blank=True)
    def __str__(self):
        return f"{self.name} - ${self.price}"

class Customer(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    address = models.TextField()
    phoneNo = PhoneNumberField(region="NZ")
    email = models.EmailField()
    def __str__(self):
        return f"{self.firstName} {self.lastName}"

class User(models.Model):
    username = models.CharField(unique=True,validators=[MinLengthValidator(8)],max_length=15)
    password = models.CharField(validators=[MinLengthValidator(8)],max_length=15)
    custID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    def __str__(self):
        return self.username

class Order(models.Model):
    custID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return f"Order by {self.customer} ({self.date})"

class Ordered_Donuts(models.Model):
    orderID = models.ForeignKey(Order, on_delete=models.CASCADE)
    flavorID = models.ForeignKey(Flavour, on_delete=models.CASCADE)
    typeID = models.ForeignKey(Type, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    def __str__(self):
        return f"{self.order} - {self.flavor} {self.type} ({self.quantity}x)"
    