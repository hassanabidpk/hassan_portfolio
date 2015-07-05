from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^/blog', views.blog, name='blog'),
    # url(r'^latest$', views.blog, name='blog'),
    # url(r'^(?P<post_id>[0-9]+)$', views.post, name='post'),
    url(r'^$', views.index, name='index'),

]