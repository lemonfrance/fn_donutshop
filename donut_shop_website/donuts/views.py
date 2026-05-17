from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from .models import Flavour, Type, Order, Customer, Ordered_Donuts
from .forms import CustomerForm, Ordered_DonutsFormSet, TYPES, FLAVOURS

# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def donuts(request):
    allTypes = Type.objects.all().values()
    allFlavours = Flavour.objects.all().values()
    
    template = loader.get_template('donuts.html')

    context = {
        'types':allTypes,
        'flavours':allFlavours,
    }

    return HttpResponse(template.render(context,request))

def details(request, id):
    rqFlavour = Flavour.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'rqFlavour':rqFlavour
    }
    return HttpResponse(template.render(context,request))

def order(request):
    if request.method=="POST":
        customerForm = CustomerForm(request.POST)
        order = Order()
        odFormset = Ordered_DonutsFormSet(request.POST,prefix='orderedDonuts',queryset=Ordered_Donuts.objects.none())

        # VALID customer
        if customerForm.is_valid() and odFormset.is_valid(): 
            customer = customerForm.save()  # Save customer to SQLite database
            customerID = get_object_or_404(Customer, id = customer.pk)

            # VALID order
            order.custID = customerID
            order.save()
            orderID = get_object_or_404(Order, id = order.pk)

            # VALID ordered donuts
            odFormset_instances = odFormset.save(commit=False)
            for od in odFormset_instances:
                typeID = TYPES.filter(id = od.typeID.pk)[0]
                flavorID = FLAVOURS.filter(id = od.flavorID.pk)[0]

                od.orderID = orderID
                od.typeID = typeID
                od.flavorID = flavorID
                
                od.save()
            return redirect('order_success')
    else: #if method == GET
        customerForm = CustomerForm()
        odFormset = Ordered_DonutsFormSet(prefix='orderedDonuts',queryset=Ordered_Donuts.objects.none())

    return render(request, 'order.html', {'customer_form': customerForm, 'orderedDonuts_formset': odFormset})

def order_success(request):
    template = loader.get_template('successfulOrder.html')
    return HttpResponse(template.render())

def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render())

def login(request):
    template = loader.get_template('login_register.html')
    return HttpResponse(template.render())