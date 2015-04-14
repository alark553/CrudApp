

from django.contrib import admin
from devices.models import Device

class deviceAdmin(admin.ModelAdmin):
    fields = ['device_name', 'range_device']
    list_display = ('device_name', 'range_device')
    list_filter = ['device_name', 'range_device']
    search_fields = ['device_name', 'range_device']

admin.site.register(Device,deviceAdmin)
