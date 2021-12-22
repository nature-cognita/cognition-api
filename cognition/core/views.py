from django.db import models
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from django_filters.rest_framework.filters import IsoDateTimeFilter
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Device, Location, Sensor, SensorRecord
from .serializers import (
    DeviceSerializer,
    LocationSerializer,
    SensorRecordSerializer,
    SensorSerializer,
)


class FilteredReadOnlyModelViewSet(ReadOnlyModelViewSet):
    filter_backends = [DjangoFilterBackend]


class LocationViewSet(ReadOnlyModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class DeviceViewSet(ReadOnlyModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ["location"]
    search_fields = ["label"]


class SensorViewSet(FilteredReadOnlyModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    filterset_fields = ["usage", "type", "device"]


class SensorRecordFilter(filters.FilterSet):
    class Meta:
        model = SensorRecord
        fields = {"timestamp": ("lte", "gte")}
        # fields = ["sensor", "location"]

    filter_overrides = {
        models.DateTimeField: {"filter_class": IsoDateTimeFilter},
    }


class SensorRecordViewSet(FilteredReadOnlyModelViewSet):
    queryset = SensorRecord.objects.all()
    serializer_class = SensorRecordSerializer
    filterset_fields = ["sensor", "location"]
    filter_class = SensorRecordFilter
