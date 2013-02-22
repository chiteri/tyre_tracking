from django.db import models

# Create your models here.
class Vehicle(models.Model): 
    VEHICLE_TYPE_CHOICES = (
        (1, u'Truck'),
        (2, u'Trailer'),
    )
    registration_number = models.CharField(max_length=9, primary_key=True)
    vehicle_type = models.IntegerField(max_length=1, choices = VEHICLE_TYPE_CHOICES )
    truck = models.ForeignKey("Vehicle", null = True, blank=True, related_name="trailer_head", help_text="Only trucks can have trailers attached to them")

    def __unicode__(self):
        return u'Truck number %s'%(self.registration_number)

class Tyre(models.Model): 
    TYRE_MANUFACTURER_CHOICES = ( 
        (u'MICH', u'MICHELLIN'),
        (u'PIRE', u'PIRELLI'),
        (u'KING', u'KINGSWAY'), 
        (u'KUMH', u'KUMHO'), 
        (u'FIRE', u'FIRESTONE'), 
        (u'YANA', u'YANA'), 
    )

    TYRE_POSITION_CHOICES = (
        (u'FRNT', u'Front Axel'),
        (u'DIFI', u'Diff Inner Axel'),
        (u'DIFO', u'Diff Outer Axel'),
        (u'OTHI', u'Other Inner Axel'),
        (u'OTHO', u'Other Outer Axel'),
    )

    TYRE_STATUS_CHOICES = (
        (u'N', u'New'), 
        (u'R', u'Retreaded'), 
        (u'W', u'Written Off / Worn Out'), 
    ) 
    serial_number = models.CharField(max_length=7, primary_key=True) 
    purchase_date = models.DateField(help_text="Date of purchase") 
    original_cost = models.IntegerField()
    make = models.CharField(max_length=4, choices = TYRE_MANUFACTURER_CHOICES, help_text="Tyre manufacturer")
    supplier = models.CharField(max_length=30, help_text="Vendor or place of purchase")
    vehicle_fitted = models.ForeignKey(Vehicle, help_text="Registration of truck fitted", null=True)
    position_fitted = models.CharField(max_length = 4, choices = TYRE_POSITION_CHOICES, null=True)
    expected_life = models.IntegerField(help_text = "Duration in mileage (Kms) for how long the tyre should last when new.") 
    retread_life = models.IntegerField(help_text = "Duration in mileage (Kms) for how long the tyre should last after retread.", null=True, blank=True)
    status = models.CharField(max_length=1, choices=TYRE_STATUS_CHOICES)
    
    def __unicode__(self): 
        return u'Tyre number %s [ %s ]'%(self.serial_number, self.make)

   
