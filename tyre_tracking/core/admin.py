from tyre_tracking.core.models import Vehicle, Tyre, Transfer
from django.contrib import admin

class VehicleAdmin(admin.ModelAdmin): 
    list_display = ('registration_number', 'vehicle_type', 'truck') 
    list_filter = ('vehicle_type',) 
    ordering = ('registration_number',) 
    search_fields = ('registration_number',)

class TyreAdmin(admin.ModelAdmin): 
    list_display = ('serial_number', 'make', 'purchase_date', 'supplier', 'original_cost', 'expected_life', 'status')
    list_filter = ('make', 'supplier', 'status',)
    ordering = ('serial_number',) 
    search_fields = ('serial_number',)
    date_hierarchy = 'purchase_date'

class TransferAdmin(admin.ModelAdmin): 
    list_display = ('transfer_date', 'tyre', 'vehicle_from', 'vehicle_to', 'tyre_state')
    list_filter = ('vehicle_from', 'vehicle_to', 'tyre_state',) 
    ordering = ('transfer_date',) 
    search_fields = ('tyre_state',) 
    date_hierarchy = 'transfer_date' 
    # fields, (to allow users to edit nothing on the transfers) 

admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Tyre, TyreAdmin)
admin.site.register(Transfer, TransferAdmin) 
