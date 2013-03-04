from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required 
from tyre_tracking.core.models import Vehicle, Tyre 
from tyre_tracking.transfer.models import Transfer

# Create your views here.
@login_required 
def home(request): 
    return render_to_response('history/history_home.html', {'user':request.user, 'vehicles': Vehicle.objects.all(), 'tyres': Tyre.objects.all() })

@login_required 
def vehicle_history(request, registration_no): 
    vehicle = Vehicle.objects.get(registration_number=registration_no)
    transfers = Transfer.objects.filter(vehicle_to=vehicle)
    transfers.order_by("-transfer_date")
    return render_to_response('history/vehicle_history.html', {'user':request.user, 'vehicle':vehicle, 'transfers':transfers}) 

@login_required 
def tyre_history(request, serial_no):
    tyre = Tyre.objects.get(serial_number=serial_no) 
    transfers = Transfer.objects.filter(tyre=tyre)
    return render_to_response('history/tyre_history.html', {'user':request.user, 'tyre':tyre, 'transfers':transfers})
