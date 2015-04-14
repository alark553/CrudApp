from django.db import models



class Device(models.Model):
    device_name = models.CharField(max_length=200)
    range_device = models.IntegerField()
    def __unicode__(self): 
       		 return self.device_name
