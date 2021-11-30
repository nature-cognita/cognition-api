from django.contrib.gis.db import models as gis_models
from django.db import models


class Plant(models.Model):
    pass


class Location(models.Model):
    name = models.CharField(max_length=120)
    coordinate = gis_models.PointField()


class SensorRecord(models.Model):
    pass
