from django.contrib import admin
from django.contrib.gis import admin as gis_admin

from .models import Device, Location, Sensor, SensorRecord


class UUIDAdmin(admin.ModelAdmin):
    readonly_fields = ("id",)


# Needed for better map preview
class LocationAdmin(gis_admin.OSMGeoAdmin):
    readonly_fields = ("id",)


admin.site.register(Device, UUIDAdmin)
admin.site.register(Sensor, UUIDAdmin)
admin.site.register(SensorRecord)


admin.site.register(Location, LocationAdmin)
