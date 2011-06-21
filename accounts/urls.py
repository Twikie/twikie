from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.views import login

urlpatterns = patterns('',
    url(r'^accounts/$', 'accounts.views.users'),
    url(r'^accounts/login/$', login),
    url(r'^accounts/register/$', 'accounts.views.registration'),
)

