from django.conf.urls import patterns, include, url
from tyre_tracking.views import hello, current_datetime, hours_ahead, display_meta 

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^hello/$', hello), 
    url(r'^time/$', current_datetime), 
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^meta/$', display_meta),
    # Examples:
    # url(r'^$', 'tyre_tracking.views.home', name='home'),
    # url(r'^tyre_tracking/', include('tyre_tracking.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
