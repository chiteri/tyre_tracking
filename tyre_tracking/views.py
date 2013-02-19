#from django.http import Http404, HttpResponse 
#from django.template import Template, Context
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response 
from django.contrib.auth.decorators import login_required 
from django.core.context_processors import csrf

def index(request): 
    if request.user.is_authenticated(): 
        return HttpResponseRedirect('/accounts/profile/')  
	
    c = {}
    c.update(csrf(request))	
    return render_to_response('base.html', c) #{'user':request.user, 'c':c }) 
	
@login_required # Decorator to denote that only authenticated / authorised users can access this view  
def home(request):
    return render_to_response('home_page.html', {'user':request.user } ) 

#def hello(request): 
#    return HttpResponse("Hello World!")

#def current_datetime(request): 
#    now = datetime.datetime.now() 
#    t = Template("<html><body>It is now {{ current_date }}. </body></html>")
#    html = t.render(Context ({'current_date':now})) 
#    return HttpResponse(html) 

#def hours_ahead(request, offset): 
#    try: 
#        offset = int(offset) 
#    except ValueError: 
#        raise Http404()

#    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
#    html = "<html><body>In %s hour(s) it will be %s</body></html>"%(offset, dt)
#    return HttpResponse(html)

#def display_meta(request):
#    values = request.META.items() 
#    values.sort() 
#    html = [] 

#    for k, v in values: 
#        html.append('<tr><td>%s</td><td>%s</td></tr>'%(k, v))

#    return HttpResponse('<table>%s</table>' % '\n'.join(html))
