from django.conf.urls import url

from . import views

urlpatterns = [
	# ex: /portfolio/ 
    url(r'^$', views.index, name='index'),
    # ex: /portfolio/5/
    url(r'^(?P<resume_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /portfolio/5/view
    url(r'^(?P<resume_id>[0-9]+)/view/$', views.view, name='view'),
    # ex /portfolio/blog
    url(r'blog/$', views.blog, name='blog'),
    #ex /portfolio/blog/5
    url(r'^blog/(?P<post_id>[0-9]+)$', views.post, name='post'),

]