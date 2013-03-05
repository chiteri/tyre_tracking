from django import template 
from tyre_tracking.core.models import Vehicle, Tyre

register = template.Library() 

@register.filter(name='vehicle_type')
def vehicle_type(code): 
    for key, value in Vehicle.VEHICLE_TYPE_CHOICES: 
        if key == code: # Compare the values passed from the templates with key 
            return value # Give the descriptive text back 
			
@register.filter(name='tyre_manufacturer')			
def tyre_manufacturer(code): 
    for key, value in Tyre.TYRE_MANUFACTURER_CHOICES: 
        if key == code: # Compare the values passed from the templates with key 
            return value # Give the descriptive text back 

@register.filter(name='tyre_position')			
def tyre_position(code): 
    for key, value in Tyre.TYRE_POSITION_CHOICES: 
        if key == code: # Compare the values passed from the templates with key 
            return value # Give the descriptive text back 

@register.filter(name='tyre_status')			
def tyre_status(code): 
    for key, value in Tyre.TYRE_STATUS_CHOICES: 
        if key == code: # Compare the values passed from the templates with key 
            return value # Give the descriptive text back 