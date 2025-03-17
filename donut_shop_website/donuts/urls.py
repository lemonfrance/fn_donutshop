from django.urls import path
from . import views

urlpatterns =[
    path('login/',views.login,name='login'),
    path('contact/',views.contact,name='contact'),
    path('order/',views.order,name='order'),
    path('donuts/',views.donuts,name='donuts'),
    path('donuts/details/<int:id>',views.details,name='details'),
    path('',views.index,name='index'),
]