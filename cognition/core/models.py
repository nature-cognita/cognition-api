import uuid

from django.contrib.gis.db import models as gis_models
from django.db import models


class UUIDModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class Location(UUIDModel):
    label = models.CharField(max_length=120)
    coordinate = gis_models.PointField()

    def __str__(self) -> str:
        return self.label


class Device(UUIDModel):
    label = models.CharField(max_length=120)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.label


class Sensor(UUIDModel):
    INTERNAL = "int"
    EXTERNAL = "ext"
    USAGE_CHOICES = [(INTERNAL, "Internal"), (EXTERNAL, "External")]

    HUMIDITY = "humid"
    LIGHT = "light"
    NOISE = "noise"
    TEMPERATURE = "temp"
    VOLTAGE = "volt"

    TYPE_CHOICES = [
        (HUMIDITY, "Humidity"),
        (LIGHT, "Light"),
        (NOISE, "Noise"),
        (TEMPERATURE, "Temperature"),
        (VOLTAGE, "Voltage"),
    ]

    usage = models.CharField(max_length=3, choices=USAGE_CHOICES, default=EXTERNAL)
    type = models.CharField(max_length=5, choices=TYPE_CHOICES)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.usage}-{self.type} on {self.device.label}"


class SensorRecord(models.Model):
    timestamp = models.DateTimeField(primary_key=True)
    value = models.FloatField()
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.timestamp} {self.sensor}"
