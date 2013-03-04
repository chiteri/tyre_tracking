from django.conf.urls import patterns, include, url
#import os 

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'tyre_tracking.views.index', name='index'), 
    url(r'^accounts/profile/$', 'tyre_tracking.views.home', name='home'), 	
    # url(r'^tyre_tracking/', include('tyre_tracking.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)), 
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', name='logout'), 
    url(r'^transfer/', include('tyre_tracking.transfer.urls')), 
    url(r'^history/', include('tyre_tracking.history.urls')), 
)
