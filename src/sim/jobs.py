import logging
from datetime import datetime, timedelta
from random import random

from api.models import Sensor
from django.conf import settings
from django.core.files.storage import default_storage


def sim_job():
    with default_storage.open(settings.SIM_FILENAME, "a") as f:
        timestamp = datetime.now()

        sensors = Sensor.objects.all()
        for s in sensors:
            sensor_id = s.id
            location_id = s.device.location.id

            sensor_value = random()
            random_delta = timedelta(milliseconds=random())

            sim_string = f"{(timestamp + random_delta).isoformat()},{sensor_id},{sensor_value},{location_id}"
            print(sim_string)

            f.write(sim_string + "\n")
