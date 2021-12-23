from core.views import (
    DeviceViewSet,
    LocationViewSet,
    SensorRecordViewSet,
    SensorViewSet,
)
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from sim.views import get_sim_data
from uploader.views import upload_file

api_router = routers.DefaultRouter()
api_router.register(r"locations", LocationViewSet)
api_router.register(r"devices", DeviceViewSet)
api_router.register(r"sensors", SensorViewSet)
api_router.register(r"records", SensorRecordViewSet)

urlpatterns = [
    path("api/", include(api_router.urls)),
    path("sim/", get_sim_data),
    path("admin/", admin.site.urls),
    path("upload/", upload_file, name="upload-file"),
]
