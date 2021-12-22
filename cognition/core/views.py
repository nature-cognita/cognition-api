from rest_framework import viewsets

from .models import Device, Location, Sensor, SensorRecord
from .serializers import (
    DeviceSerializer,
    LocationSerializer,
    SensorRecordSerializer,
    SensorSerializer,
)


class LocationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class DeviceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class SensorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorRecordViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SensorRecord.objects.all()
    serializer_class = SensorRecordSerializer
