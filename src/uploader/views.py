import csv
from datetime import datetime

from core.models import Location, Sensor, SensorRecord
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.timezone import make_aware

from .forms import UploadFileForm


def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            data_file = form.save()

            with data_file.file.open(mode="r") as f:
                reader = csv.reader(f)

                for row in reader:
                    timestamp, sensor_id, sensor_value, location_id = row

                    print(sensor_id)

                    sensor_record = SensorRecord(
                        timestamp=make_aware(datetime.fromisoformat(timestamp)),
                        sensor=Sensor(id=sensor_id),
                        value=sensor_value,
                        location=Location(id=location_id),
                    )

                    sensor_record.save()

            return HttpResponseRedirect("/upload/")
    else:
        form = UploadFileForm()
    return render(request, "upload.html", {"form": form})
