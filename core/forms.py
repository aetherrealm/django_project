from django import forms
from .models import IP_Addresses, VLANs

class CoreForm(forms.Form):
    vid = forms.ModelChoiceField(queryset=VLANs.objects.all())
    evpn = forms.BooleanField()
    anycast_gateway = forms.ModelChoiceField(queryset=IP_Addresses.objects.all())