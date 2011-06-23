from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.views import login

urlpatterns = patterns('',
    url(r'^$', 'accounts.views.users'),
    url(r'^login/$', login),
    url(r'^register/$', 'accounts.views.registration'),
)

