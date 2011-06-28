from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('',
    url(r'^all', 'django_pm.views.index'),
    url(r'^new', 'django_pm.views.newmessage'),
    url(r'^(?P<message_id>\d+)/$', 'django_pm.views.message'),
)

