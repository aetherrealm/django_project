from django import forms
from .models import IP_Addresses

class CoreForm(forms.Form):
    IPs = forms.ModelChoiceField(queryset=IP_Addresses.objects.all())