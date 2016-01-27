from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse,Http404
from django.template import RequestContext, loader


from .models import Post, News, Skill,Project
from mooc.models import MOOC

def index(request):
	skills = Skill.objects.order_by('title')
	projects = Project.objects.order_by('createdAt')
	blog_posts = Post.objects.order_by('-post_published')
	moocs = MOOC.objects.order_by('course_completion_date')
	context = {"skills": skills,"projects": projects,'blog_posts': blog_posts,'moocs':moocs}
	return render(request,'portfolio/index_mat.html', context)

def blog(request):
	blog_posts = Post.objects.order_by('-post_published')
	context = {'blog_posts': blog_posts}
	return render(request, 'portfolio/blog_home_mat.html', context)


def post(request,post_id):
	post = get_object_or_404(Post,pk=post_id)
	categories = post.category.all()
	print(categories)
	return render(request, 'portfolio/entry_mat.html', {'post': post,'categories':categories})
