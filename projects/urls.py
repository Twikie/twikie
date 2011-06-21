from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^projects/$', 'projects.views.index'),
    url(r'^projects/(?P<project_id>\d+)/$', 'projects.views.detail'),
    url(r'^projects/(?P<project_id>\d+)/revisions/new/$', 'projects.views.newrev'),
    url(r'^projects/(?P<project_id>\d+)/revisions/(?P<rev_id>\d+)/$', 'projects.views.rev'),
    url(r'^projects/new', 'projects.views.new'),
)

