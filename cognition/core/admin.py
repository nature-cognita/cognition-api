from django.contrib import admin
from django.contrib.gis import admin as gis_admin
from django.core.exceptions import PermissionDenied

from .models import Device, Location, Sensor, SensorRecord


class UUIDAdmin(admin.ModelAdmin):
    readonly_fields = ("id",)


# Needed for better map preview
class LocationAdmin(gis_admin.OSMGeoAdmin):
    readonly_fields = ("id",)


admin.site.register(Device, UUIDAdmin)
admin.site.register(Sensor, UUIDAdmin)


@admin.action(description="Delete selected timestamped sensor records")
def delete_model(modeladmin, request, queryset):
    if not modeladmin.has_delete_permission(request):
        raise PermissionDenied
    for obj in queryset:
        obj.delete()


class SensorRecordAdmin(admin.ModelAdmin):
    def get_actions(self, request):
        actions = super().get_actions(request)
        if "delete_selected" in actions:
            del actions["delete_selected"]
        return actions

    actions = [delete_model]


admin.site.register(SensorRecord, SensorRecordAdmin)


admin.site.register(Location, LocationAdmin)
