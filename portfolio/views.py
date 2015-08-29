from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse,Http404
from django.template import RequestContext, loader


from .models import Blog, News

def index(request):
	context = ''
	return render(request,'portfolio/index.html', context)

def blog(request):
	blog_posts = Blog.objects.order_by('-post_published')
	context = {'blog_posts': blog_posts}
	return render(request, 'portfolio/blog_home_mat.html', context)


def post(request,post_id):
	post = get_object_or_404(Blog,pk=post_id)
	return render(request, 'portfolio/entry_mat.html', {'post': post})


	
