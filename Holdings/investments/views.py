from django.http import HttpResponse

def index(request):
	return HttpResponse ("Welcome to Investments.")
# Create your views here.
