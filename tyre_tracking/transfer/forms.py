from django import forms 
from tyre_tracking.core.models import Tyre #, Vehicle 

class TransferForm(forms.ModelForm):
    # Add some custom validations to the form 
    def clean(self): 
        data = self.cleaned_data
        modified_tyre = data["tyre"] 
        	
        # Make sure that the tyre is moving to a new position, if on the same vehicle 
        if modified_tyre.vehicle_fitted == data["vehicle_to"] and modified_tyre.position_fitted == data["new_position"]: 
            raise forms.ValidationError('Tyre is moving from [ %s ] to [ %s ] which is identical'% (modified_tyre.position_fitted, data["new_position"]))
					
        # If missing vehicle to, then tyre's new position is not a-must but its status is mandatory and should change (retread, written off) 
        if not data["vehicle_to"] and data["new_position"]: 
            raise forms.ValidationError('Tyre cannot go to position [ %s ] if it is missing a vehicle to.'% data["new_position"]) 
        elif not data["vehicle_to"] and not data["tyre_state"]:
            raise forms.ValidationError('Tyre cannot go miss both a vehicle to and a new status.') 
				
        # You should specify the new position of a tyre when assigning it to a vehicle
        if data["vehicle_to"] and not data["new_position"]:			
            raise forms.ValidationError('You should specify a new tyre position on %s.'%data["vehicle_to"]) 
			
		# A tyre that is being written off cannot be assigned to a vehicle  
        if data["tyre_state"] == Tyre.TYRE_STATUS_CHOICES[2][0] and data["vehicle_to"]: 
            raise forms.ValidationError('A Tyre that is %s cannot be assigned to %s.'%(Tyre.TYRE_STATUS_CHOICES[2][1], data["vehicle_to"]))
			
        # A tyre that has been written off cannot be move to another vehicle, only from 
        if modified_tyre.status == Tyre.TYRE_STATUS_CHOICES[2][0]: 
            raise forms.ValidationError('Tyre %s is written off and cannot be put back on %s.'%(modified_tyre.serial_number, data["vehicle_to"]))
			
        return data 