from django.contrib.gis import admin

from .models import Device, Location, Sensor

admin.site.register(Device)
admin.site.register(Sensor)


class LocationAdmin(admin.OSMGeoAdmin):
    pass


admin.site.register(Location, LocationAdmin)
