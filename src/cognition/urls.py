from api.views import (DeviceViewSet, LocationViewSet, SensorRecordViewSet,
                       SensorViewSet)
from django.contrib import admin
from django.urls import include, path
from map.views import display_map
from nft.views import ImageNFTViewSet, display_nft
from nft_generator.views import generate_nft, generator_success
from rest_framework import routers
from sim.views import get_sim_data
from uploader.views import upload_file

api_router = routers.DefaultRouter()
api_router.register(r"locations", LocationViewSet)
api_router.register(r"devices", DeviceViewSet)
api_router.register(r"sensors", SensorViewSet)
api_router.register(r"records", SensorRecordViewSet)
api_router.register(r"nfts", ImageNFTViewSet)

urlpatterns = [
    path("api/", include(api_router.urls)),
    path("sim/", get_sim_data),
    path("admin/", admin.site.urls),
    path("upload/", upload_file, name="upload-file"),
    path("map/", display_map),
    path("nft/", display_nft),
    path("generator/", generate_nft, name="generator"),
    path("generator-success/", generator_success, name="generator-success"),
]
