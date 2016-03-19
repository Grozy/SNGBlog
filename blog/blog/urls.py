from django.conf.urls import patterns, include, url
from django.contrib import admin
import  settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url('^markdown/', include( 'django_markdown.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog$', 'sblog.views.blog_list', name='blog_list'),
    url(r'^$', 'sblog.views.index', name='index'),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_PATH}),
    url(r'^blog/(?P<blog_id>[0-9]*)$', 'sblog.views.blog', name='blog'),

)
