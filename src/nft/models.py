from django.db import models


class ImageNFT(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    data = models.TextField()
    image_url = models.CharField(max_length=300, default="")
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
