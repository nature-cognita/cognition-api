from core.views import LocationViewSet
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from sim.views import get_sim_data
from uploader.views import upload_file

router = routers.DefaultRouter()
router.register(r"locations", LocationViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path("sim/", get_sim_data),
    path("admin/", admin.site.urls),
    path("upload/", upload_file, name="upload-file"),
]
