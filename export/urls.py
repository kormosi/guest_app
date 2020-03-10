from django.urls import path
from . import views

urlpatterns = [
    path('', views.export, name='export-home')
]
