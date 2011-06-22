from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'projects.views.detail'),
    url(r'^pages/new/$', 'projects.views.newpage'),
    url(r'^new', 'projects.views.new'),
    url(r'^(?P<page_name>\w+)/$', 'projects.views.page'),
)

