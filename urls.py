from django.conf.urls.defaults import patterns, include, url

from django.conf import settings

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

    url(r'^inbox/', include('django_pm.urls')),
    
    url(r'^accounts/', include('accounts.urls')),
    url(r'^(?P<user_name>[-\w]+)/$', 'accounts.views.profile'),
    
    url(r'^projects/', include('frat.urls')),
    url(r'^(?P<user_name>[-\w]+)/(?P<project_slug>[-\w]+)/', include('frat.urls')),
    
    url(r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'base.html'}),
    
    
    #needs to be last
    #url(r'^', 'django.views.generic.simple.direct_to_template', {'template': 'base.html'}),
    
    # Examples:
    # url(r'^$', 'twikie.views.home', name='home'),
    # url(r'^twikie/', include('twikie.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)



#BAD.
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )

