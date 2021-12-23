from datetime import datetime
from random import random

from api.models import Sensor
from django.conf import settings
from django.core.files.storage import default_storage


def sim_job():
    print(settings.BASE_DIR)
    with default_storage.open(settings.SIM_FILENAME, "a") as f:
        timestamp = datetime.now().isoformat()

        sensors = Sensor.objects.all()

        for s in sensors:
            sensor_id = s.id
            location_id = s.device.location.id
            sensor_value = random()

            sim_string = f"{timestamp},{sensor_id},{sensor_value},{location_id}"
            print(sim_string)
            f.write(sim_string + "\n")
