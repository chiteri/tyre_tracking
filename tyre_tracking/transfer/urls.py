from django.conf.urls import patterns, include, url 
from tyre_tracking.transfer.models import Transfer

#transfer_info = {
#    'queryset': Transfer.objects.all(),
#}

urlpatterns = patterns('',
    url(r'^$', 'tyre_tracking.transfer.views.home', name='home'), 	
    url(r'^success/$', 'tyre_tracking.transfer.views.success', name='success'), 	
)

