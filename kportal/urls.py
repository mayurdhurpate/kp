from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'content.views.home', name='home'),
    url(r'^test$', 'content.views.test', name='test'),
    url(r'^content/$', 'content.views.details', name='details'),
    url(r'^content1/$', 'content.views.details1', name='details1'),
    url(r'^publish/$', 'content.views.publish', name='publish'),
    url(r'^dashboard/$', 'content.views.dashboard', name='dashboard'),
    url(r'^asd/$', 'content.views.asd', name='asd'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
