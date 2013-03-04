from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required 
from tyre_tracking.core.models import Vehicle, Tyre 

# Create your views here.
@login_required 
def home(request): 
    return render_to_response('history/history_home.html', {'vehicles': Vehicle.objects.all(), 'tyres': Tyre.objects.all() })
