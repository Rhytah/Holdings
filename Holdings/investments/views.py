from django.http import HttpResponse
from django.template import loader
from django.views import generic

from .models import Item 

def index(request):
	template = loader.get_template('investments/index.html')
#	return HttpResponse ("Welcome to Investments.")
	return render(request,'investments/html')
	
def items(request):
	response ="A few of the vendors"
	return HttpResponse(response)

def services(request, ):
	response = "VArious services"
	return HttpResponse(response)

def look(request):
	return HttpResponse("See for yourself")

#def index(request):
#	return HttpResponse ("Welcome to Investments.")

# Create your views here.
