from django.http import HttpResponse
from django.template import loader
from .models import Flavour, Type

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
    allTypes = Type.objects.all().values()
    allFlavours = Flavour.objects.all().values()
    
    template = loader.get_template('order.html')

    context = {
        'types':allTypes,
        'flavours':allFlavours,
    }

    return HttpResponse(template.render(context,request))

def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render())

def login(request):
    template = loader.get_template('login_register.html')
    return HttpResponse(template.render())