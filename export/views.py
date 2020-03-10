from django.shortcuts import render
from django.http import HttpResponse, request

guests = [
    {
        'firstname':'patrik',
        'lastname' : 'kormosi',
        'base64' : '7c1ff34e630a11eabc550242ac130003'
    },
    {
        'firstname':'patrik',
        'lastname' : 'kormosi',
        'base64' : '7c1ff34e630a11eabc550242ac130003'
    },
    {
        'firstname':'patrik',
        'lastname' : 'kormosi',
        'base64' : '7c1ff34e630a11eabc550242ac130003'
    },
    {
        'firstname':'patrik',
        'lastname' : 'kormosi',
        'base64' : '7c1ff34e630a11eabc550242ac130003'
    },
    {
        'firstname':'patrik',
        'lastname' : 'kormosi',
        'base64' : '7c1ff34e630a11eabc550242ac130003'
    }
]

def export(request):
    context = {
        'guests' : guests
    }
    return render(request, 'export/index.html', context)
