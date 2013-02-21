from django.shortcuts import render_to_response 
from django.contrib.auth.decorators import login_required 
from django.forms.models import modelformset_factory
from tyre_tracking.core.models import Transfer
from django.core.context_processors import csrf 
from django.http import HttpResponseRedirect  
# from django.forms import Textarea

# Create your views here.

@login_required # Decorator to denote that only authenticated / authorised users can access this view  
def home(request):
    # TransferFormSet = modelformset_factory(Transfer, widgets={"transfer_date": Textarea(), "class":'datePicker', "readonly":'true'}) 
    TransferFormSet = modelformset_factory(Transfer)
    context = {}
    context.update(csrf(request))	
	
    if request.method == 'POST': 		
        formset = TransferFormSet(request.POST, request.FILES)
		
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect('/transfer/success/') 
    else:
        formset = TransferFormSet(queryset=Transfer.objects.none())
		
    return render_to_response('transfer/transfer_home.html', 
	dict({'user':request.user, 'formset': formset, 'transfers':Transfer.objects.all() }.items() + context.items())) # merge the two dictionaries 
	
@login_required # Decorator to denote that only authenticated / authorised users can access this view  
def success(request): 
    return render_to_response('transfer/transfer_success.html')