from django import forms
from .models import IP_Addresses

class CoreForm(forms.Form):
    IPs = forms.ModelMultipleChoiceField(
            queryset=IP_Addresses.objects.all(),
            widget=forms.CheckboxSelectMultiple,
            label="Select Tags"
        )