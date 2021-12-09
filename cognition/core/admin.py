from django.contrib.gis import admin

from .models import Device, Location, Sensor, SensorRecord


class UUIDAdmin(admin.ModelAdmin):
    readonly_fields = ("id",)


# Needed for better map preview
class LocationAdmin(admin.OSMGeoAdmin):
    readonly_fields = ("id",)


admin.site.register(Device, UUIDAdmin)
admin.site.register(Sensor, UUIDAdmin)
admin.site.register(SensorRecord)


admin.site.register(Location, LocationAdmin)
