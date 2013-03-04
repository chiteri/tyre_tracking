from django.conf.urls import patterns, include, url 
from tyre_tracking.transfer.models import Transfer
from tyre_tracking.core.models import Vehicle, Tyre 

#transfer_info = {
#    'queryset': Transfer.objects.all(),
#}

urlpatterns = patterns('',
    url(r'^$', 'tyre_tracking.history.views.home', name='home'), 	
    url(r'^vehicle/(?P<registration_no>[^/]+)/$', 'tyre_tracking.history.views.vehicle_history', name='vehicle_history'), 	
    url(r'^tyre/(?P<serial_no>[\w]+)/$', 'tyre_tracking.history.views.tyre_history', name='tyre_history'), 	
)

