from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('',
    
    url(r'^new', 'django_pm.views.newmessage'),
    url(r'^(?P<message_id>\d+)/$', 'django_pm.views.message'),
    url(r'^', 'django_pm.views.index'),
)

