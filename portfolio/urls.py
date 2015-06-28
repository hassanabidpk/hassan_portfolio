from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^/blog', views.blog, name='blog'),
    url(r'^$', views.blog, name='blog'),
    # url(r'^$', views.index, name='index'),
    url(r'^(?P<post_id>[0-9]+)$', views.post, name='post'),

]