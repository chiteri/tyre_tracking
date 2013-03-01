from django.db import models
from django.contrib.auth.models import User 
from tyre_tracking.core.models import Vehicle, Tyre 
import datetime

# Create your models here.

class Transfer(models.Model): 
    agent = models.ForeignKey(User, help_text = "The person who effected the transfer", unique=False, related_name='transfer_agent')
    transfer_date = models.DateField(help_text="Date transfer was effected", blank=False, null=False, default=datetime.datetime.now) 
    tyre =  models.ForeignKey(Tyre, help_text="Tyre transferred") 
    # vehicle_from = models.ForeignKey(Vehicle, related_name="transfer_from", null=True, blank=True) 
    vehicle_to = models.ForeignKey(Vehicle, related_name="transfer_to", null=True, blank=True) 
    new_position = models.CharField(max_length=4, choices = Tyre.TYRE_POSITION_CHOICES, null=True, blank=True) 
    tyre_state =  models.CharField(max_length=1, choices = Tyre.TYRE_STATUS_CHOICES)

    def __unicode__(self): 
        return u"%s transfer [%s]"%(self.transfer_date, self.vehicle_from)
