from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'projects.views.index'),
    url(r'^(?P<project_id>\d+)/$', 'projects.views.detail'),
    url(r'^(?P<project_id>\d+)/revisions/new/$', 'projects.views.newrev'),
    url(r'^(?P<project_id>\d+)/revisions/(?P<rev_id>\d+)/$', 'projects.views.rev'),
    url(r'^new', 'projects.views.new'),
)

