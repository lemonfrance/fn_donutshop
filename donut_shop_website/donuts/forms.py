from django import forms
from django.forms import modelformset_factory
from .models import Customer, Ordered_Donuts
from .models import Flavour, Type, Order
from phonenumber_field.formfields import PhoneNumberField

TYPES = Type.objects.all()
FLAVOURS = Flavour.objects.all()
ORDERS = Order.objects.all()

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['firstName', 'lastName', 'address', 'phoneNo', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'autocomplete':'on'}),
            'last_name': forms.TextInput(attrs={'autocomplete':'on'}),
            'address': forms.Textarea(attrs={'autocomplete':'on'}),
            'phone': PhoneNumberField(region='NZ',help_text="You are required to enter a valid NZ phone number."),
            'email': forms.EmailInput(attrs={'autocomplete':'on'})
        }

class Ordered_DonutsForm(forms.ModelForm):
    class Meta:
        model = Ordered_Donuts
        fields = ['orderID','typeID','flavorID','quantity']
        widgets = {
            'quantity': forms.NumberInput(attrs={'min':'1', 'value':'1'})
        }
    def __init__(self, *args, **kwargs):
        super(Ordered_DonutsForm, self).__init__(*args, **kwargs)
        self.fields['orderID']= forms.ModelChoiceField(ORDERS,required=False, widget=forms.HiddenInput())
        self.fields['typeID']=forms.ModelChoiceField(TYPES, label="Type", widget=forms.Select(attrs={'autocomplete':'on'}))
        self.fields['flavorID']=forms.ModelChoiceField(FLAVOURS, label="Flavour", widget=forms.Select(attrs={'autocomplete':'on'}))
        self.fields['typeID'].label_from_instance = self.label_from_instance
        self.fields['flavorID'].label_from_instance = self.label_from_instance
    @staticmethod
    def label_from_instance(obj):
        return obj.name

Ordered_DonutsFormSet = modelformset_factory(Ordered_Donuts, form=Ordered_DonutsForm, extra=1)