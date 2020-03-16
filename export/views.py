from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from .models import Guest
from weasyprint import HTML

def home(request):

    if request.method == 'POST' and 'export_to_pdf' in request.POST:

        # Model data.
        guests = Guest.objects.all()

        # Rendering HTML.
        html_string = render_to_string('export/export.html', {'guests': guests})

        # Creating HTTP PDF response.
        response = HttpResponse(content_type='application/pdf;')
        response['Content-Disposition'] = 'attachment; filename=guests.pdf'
        HTML(string=html_string).write_pdf(response)

        return response

    else:
        # Model data
        guests = Guest.objects.all()[:100]
        return render(request, 'export/index.html', {'guests':guests})
