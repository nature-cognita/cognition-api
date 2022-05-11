from rest_framework.serializers import ModelSerializer

from .models import ImageNFT


class ImageNFTSerializer(ModelSerializer):
    class Meta:
        model = ImageNFT
        fields = "__all__"
        read_only_fields = ["id", "generator_id", "created_at"]
