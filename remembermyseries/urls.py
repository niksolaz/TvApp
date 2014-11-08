from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'remembermyseries.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^tvapp/', include('tvapp.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
