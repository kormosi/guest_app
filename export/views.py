from django.shortcuts import render
from .models import Guest

def export(request):
    context = {
        'guests' : Guest.objects.all()
    }
    return render(request, 'export/index.html', context)
