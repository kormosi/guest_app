from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Guest

def export(request):

    if request.method == 'POST':
        # Import function to run.
        from export.weasy import Weasy
        # Call function.
        Weasy.weasy()
        # Display success message.
        messages.success(request, f'Your PDF is ready, click to downlaod.')
        return redirect('export-home')

    else:

        context = {
            'guests' : Guest.objects.all()[:100]
        }

        return render(request, 'export/index.html', context)
