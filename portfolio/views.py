from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse,Http404
from django.template import RequestContext, loader


from .models import Resume, Blog, News

def index(request):
	latest_resume_list = Resume.objects.order_by('-pub_date')[:5]
	# ouput = ', '.join([(p.first_name + " " + p.last_name) for p in latest_resume_list])
	# return HttpResponse("Hello, world. You 're at the Portfolio")
	# return HttpResponse(ouput)
	# template = loader.get_template('portfolio/index.html')
	context = RequestContext(request, {
		'latest_resume_list' : latest_resume_list,
		})
	# return HttpResponse(template.render(context))
	return render(request,'portfolio/index.html', context)


def detail(request,resume_id):
	# try:
	# 	resume = Resume.objects.get(pk=resume_id)
	# except Resume.DoesNotExist:
	# 	raise Http404("Resume does not exit")
	resume = get_object_or_404(Resume,pk=resume_id)	
	# return HttpResponse("You're looking at Resume %s." % resume_id)
	return render(request,'portfolio/detail.html', {'resume' : resume})


def view(request,resume_id):
	return HttpResponse("You 're looking at views for resume of %s." % resume_id)

def blog(request):
	# post = get_object_or_404(Blog,pk=post_id)
	return HttpResponse("You 're looking at post with id %s." % "blog")

def post(request,post_id):
	post = get_object_or_404(Blog,pk=post_id)
	return render(request, 'portfolio/singlepost.html', {'post': post})
