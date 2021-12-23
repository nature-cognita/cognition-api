import uuid
from datetime import timedelta

from django.contrib.gis.db import models as gis_models
from django.db import IntegrityError, models
from django.utils.dateparse import parse_datetime


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
    location = models.ForeignKey(
        Location, related_name="devices", on_delete=models.CASCADE
    )

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
    device = models.ForeignKey(Device, related_name="sensors", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.usage}-{self.type} on {self.device.label}"


class SensorRecord(models.Model):
    timestamp = models.DateTimeField(primary_key=True)
    value = models.FloatField()
    sensor = models.ForeignKey(Sensor, related_name="records", on_delete=models.CASCADE)
    location = models.ForeignKey(
        Location, related_name="records", on_delete=models.CASCADE
    )

    def save_and_smear_timestamp(self, *args, **kwargs):
        """Recursivly try to save by incrementing the timestamp on duplicate error"""
        try:
            super().save(*args, **kwargs)
        except IntegrityError as exception:
            # Only handle the error:
            #   psycopg2.errors.UniqueViolation: duplicate key value violates unique constraint "1_1_farms_sensorreading_pkey"
            #   DETAIL:  Key ("time")=(2020-10-01 22:33:52.507782+00) already exists.
            if all(k in exception.args[0] for k in ("Key", "time", "already exists")):
                # Increment the timestamp by 1 µs and try again
                self.time = str(parse_datetime(self.time) + timedelta(microseconds=1))
                self.save_and_smear_timestamp(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.timestamp} {self.sensor}"
