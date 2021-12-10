import os

from django.conf import settings
from django.core.files.storage import default_storage
from django.http import FileResponse

sim_filename = settings.SIM_FILENAME


class SimResponse(FileResponse):
    def close(self):
        super().close()
        os.remove(default_storage.path(sim_filename))


def get_sim_data(request):
    return SimResponse(default_storage.open(sim_filename, "rb"), as_attachment=True)
