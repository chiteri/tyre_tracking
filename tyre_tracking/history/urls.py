from django.conf.urls import patterns, include, url 
from tyre_tracking.transfer.models import Transfer
from tyre_tracking.core.models import Vehicle, Tyre 

#transfer_info = {
#    'queryset': Transfer.objects.all(),
#}

urlpatterns = patterns('',
    url(r'^$', 'tyre_tracking.history.views.home', name='home'), 	
    url(r'^vehicle/$', 'tyre_tracking.transfer.views.success', name='success'), 	
    url(r'^tyre/$', 'tyre_tracking.transfer.views.success', name='success'), 	
)

