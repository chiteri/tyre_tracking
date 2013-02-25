from tyre_tracking.core.models import Vehicle, Tyre
from django.contrib import admin

class VehicleAdmin(admin.ModelAdmin): 
    list_display = ('registration_number', 'vehicle_type', 'truck') 
    list_filter = ('vehicle_type',) 
    ordering = ('registration_number',) 
    search_fields = ('registration_number',)

class TyreAdmin(admin.ModelAdmin): 
    list_display = ('serial_number', 'make', 'vehicle_fitted', 'position_fitted', 'purchase_date', 'supplier', 'original_cost', 'expected_life', 'retread_life', 'status')
    list_filter = ('make', 'supplier', 'status',)
    ordering = ('serial_number',) 
    search_fields = ('serial_number',)
    date_hierarchy = 'purchase_date'

admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Tyre, TyreAdmin)

