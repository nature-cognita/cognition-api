from rest_framework.serializers import ModelSerializer
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from .models import Device, Location, Sensor, SensorRecord


# TODO: Make it hyperlinked
class LocationSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Location
        geo_field = "coordinate"
        fields = [
            "id",
            "label",
            "coordinate",  # TODO: Rename to geometry
            "devices",
        ]


class DeviceSerializer(ModelSerializer):
    class Meta:
        model = Device
        fields = ["id", "label", "location", "sensors"]


class SensorSerializer(ModelSerializer):
    class Meta:
        model = Sensor
        fields = ["id", "usage", "type", "device"]


class SensorRecordSerializer(ModelSerializer):
    class Meta:
        model = SensorRecord
        fields = ["timestamp", "value", "sensor", "location"]
