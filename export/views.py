from django.shortcuts import render
from .models import Guest

def export(request):

    context = {
        'guests' : Guest.objects.all()[:100]
    }
    return render(request, 'export/index.html', context)


def weasy_view(request):

    if request.method == 'POST':

        # import function to run
        from export.weasy import Weasy

        # call function
        Weasy.weasy()

        # return user to required page
        context = {
            'guests' : Guest.objects.all()[:10]
        }

        return render(request, 'export/index.html', context)
