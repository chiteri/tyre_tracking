from django.shortcuts import render_to_response 
from django.contrib.auth.decorators import login_required 
from django.forms.models import modelformset_factory
from tyre_tracking.transfer.models import Transfer 
from tyre_tracking.core.models import Tyre, Vehicle 
from django.core.context_processors import csrf 
from django.http import HttpResponseRedirect 
from tyre_tracking.transfer.forms import TransferForm 
# from django.forms import Textarea

# Create your views here.
@login_required # Decorator to denote that only authenticated / authorised users can access this view  
def home(request):
    # TransferFormSet = modelformset_factory(Transfer, widgets={"transfer_date": Textarea(), "class":'datePicker', "readonly":'true'}) 
    TransferFormSet = modelformset_factory(Transfer, form=TransferForm)
    context = {}
    context.update(csrf(request))	
			
    if request.method == 'POST': 		
        formset = TransferFormSet(request.POST, request.FILES) 
		
        if formset.is_valid():
            formset.save() 
			
            # Move the tyre to another vehicle if possible and change its position and status, unless it has bee written off  
			# try: 
            changed_tyre = Tyre.objects.get(serial_number=request.POST['form-0-tyre'] ) 
			
            changed_tyre.vehicle_fitted = Vehicle.objects.get(registration_number=request.POST['form-0-vehicle_to']) if request.POST['form-0-vehicle_to'] else None
            changed_tyre.position_fitted=request.POST['form-0-new_position'] if request.POST['form-0-new_position'] else None 
            changed_tyre.status=request.POST['form-0-tyre_state']  
            changed_tyre.save() 
			
            return HttpResponseRedirect('/transfer/success/') 
            # except: 
    else:
        formset = TransferFormSet(queryset=Transfer.objects.none())
		
    return render_to_response('transfer/transfer_home.html', 
	dict({'user':request.user, 'formset': formset, 'transfers':Transfer.objects.all() }.items() + context.items())) # merge the two dictionaries 
	
@login_required # Decorator to denote that only authenticated / authorised users can access this view  
def success(request): 
    return render_to_response('transfer/transfer_success.html')