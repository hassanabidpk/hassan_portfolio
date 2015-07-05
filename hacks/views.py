from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse,Http404
from django.template import RequestContext, loader


from .models import Hack

def index(request):

	context = ""
	return render(request,'hacks/index.html', context)