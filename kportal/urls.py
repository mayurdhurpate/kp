from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'content.views.home', name='home'),
    url(r'^publish/$', 'content.views.publish', name='publish'),
    url(r'^dashboard/$', 'content.views.dashboard', name='dashboard'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

