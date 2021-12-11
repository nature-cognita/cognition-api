from django.db import models


class DataFile(models.Model):
    file = models.FileField()
