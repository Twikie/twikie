from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.views import login
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^accounts/', include('accounts.urls'),
    url(r'^projects/', include('projects.urls'),
    # Examples:
    # url(r'^$', 'twikie.views.home', name='home'),
    # url(r'^twikie/', include('twikie.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
