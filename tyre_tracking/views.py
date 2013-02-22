from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response 
from django.contrib.auth.decorators import login_required 
from django.core.context_processors import csrf

def index(request): 
    if request.user.is_authenticated(): 
        return HttpResponseRedirect('/accounts/profile/')  
	
    c = {}
    c.update(csrf(request))	
    return render_to_response('base.html', c)  
	
@login_required # Decorator to denote that only authenticated / authorised users can access this view  
def home(request):
    return render_to_response('home_page.html', {'user':request.user } )  
    