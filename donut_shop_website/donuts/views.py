from django.http import HttpResponse
from django.template import loader
from .models import Flavour, Type

# Create your views here.

def donuts(request):
    allTypes = Type.objects.all().values()
    allFlavours = Flavour.objects.all().values()
    
    template = loader.get_template('donuts.html')

    context = {
        'types':allTypes,
        'flavours':allFlavours,
    }

    return HttpResponse(template.render(context,request))

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())