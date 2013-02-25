from django.contrib import admin 
from tyre_tracking.transfer.models import Transfer

class TransferAdmin(admin.ModelAdmin): 
    list_display = ('transfer_date', 'agent', 'tyre', 'vehicle_from', 'vehicle_to', 'new_position', 'tyre_state')
    list_filter = ('vehicle_from', 'vehicle_to', 'tyre_state') 
    ordering = ('-transfer_date',) 
    search_fields = ('tyre_state',) 
    date_hierarchy = 'transfer_date' 
    # fields, (to allow users to edit nothing on the transfers) 
	
admin.site.register(Transfer, TransferAdmin) 