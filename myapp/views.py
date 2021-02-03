from django.shortcuts import render
#importing loading from django template
from django.template import loader
from myapp.form import StudentForm
from myapp.functions.functions import handle_uploaded_file
# Create your views here.
from django.http import HttpResponse
from myapp.models import Employee
from django.core.exceptions import ObjectDoesNotExist
import csv
from myapp.models import Employee
from reportlab.pdfgen import canvas


def getfile(request):
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment'; filename = 'file.pdf'
	p = canvas.Canvas(response)
	p.setFont('Times-Roman', 55)
	p.drawString(100, 700, 'Hello, Chintan')
	p.showPage()
	p.save()
	return response

def index(request):
	return render(request, 'index.html')
