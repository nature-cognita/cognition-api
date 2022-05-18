from urllib.parse import urljoin

from django.conf import settings
from django.db import models


class ImageNFT(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    data = models.TextField()
    image_url = models.CharField(max_length=300, default="")
    user = models.CharField(max_length=300, default="None")

    @property
    def absolute_url(self):
        return urljoin(settings.ONE_MODEL_URL, self.image_url)

    CREATED = "created"
    GENERATED = "generated"
    ERROR = "error"
    STATUS_CHOICES = [
        (CREATED, "Created"),
        (GENERATED, "Generated"),
        (ERROR, "Error"),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=CREATED)
    error = models.TextField(default="")
