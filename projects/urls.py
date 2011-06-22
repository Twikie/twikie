from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'projects.views.index'),
    url(r'^(?P<project_id>\d+)/$', 'projects.views.detail'),
    url(r'^(?P<project_id>\d+)/pages/new/$', 'projects.views.newpage'),
    url(r'^(?P<project_id>\d+)/pages/(?P<page_id>\d+)/$', 'projects.views.page'),
    url(r'^new', 'projects.views.new'),
)

