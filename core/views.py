from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from . import forms

class CoreView(View):
    def get(self, request):
        
        form = forms.CoreForm
        return render(request, "core/core.html", {"form": form})

    def post(self, request):

        return HttpResponse("Submitted.")
