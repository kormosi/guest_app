from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.template.loader import render_to_string
from .models import Guest
from weasyprint import HTML
import tempfile


def home(request):

    if request.method == 'POST' and 'export_to_pdf' in request.POST:

        # Model data.
        guests = Guest.objects.all()[:50]

        # Rendering HTML.
        html_string = render_to_string('export/export.html', {'guests': guests})
        html = HTML(string=html_string)
        rendered_result = html.write_pdf()

        # Creating HTTP response.
        response = HttpResponse(content_type='application/pdf;')
        response['Content-Disposition'] = 'attachment; filename=guests.pdf'

        # Writing rendered result into temporary file and serving it to user.
        with tempfile.NamedTemporaryFile(delete=True) as file:
            file.write(rendered_result)
            file.flush()
            file = open(file.name, 'rb')
            response.write(file.read())

        return response

    else:
        # Model data
        guests = Guest.objects.all()[:100]
        return render(request, 'export/index.html', {'guests':guests})
