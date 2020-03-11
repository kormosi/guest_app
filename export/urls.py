from django.urls import path
from . import views

urlpatterns = [
    path('', views.export, name='export-home'),
    # TODO toto ked tak vymazat
    path('weasy/', views.weasy_view, name='export-weasy')
]
