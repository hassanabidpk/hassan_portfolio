from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'hassan_portfolio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('portfolio.urls', namespace="portfolio")),
    url(r'^blog/', include('portfolio.urls', namespace="portfolio")),

]
