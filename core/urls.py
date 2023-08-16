from . import views
from django.urls import path

urlpatterns = [
    path('', views.CoreView.as_view(), name = 'core')
]