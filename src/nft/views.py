from typing import Dict
from urllib.parse import urljoin

import requests
from django.conf import settings
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import ImageNFT
from .serializers import ImageNFTSerializer


class ImageNFTViewSet(ModelViewSet):
    """
    List available NFTs or create new one.
    """

    queryset = ImageNFT.objects.all().order_by("-created_at")
    serializer_class = ImageNFTSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["status"]

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            validated_data: Dict = serializer.validated_data

            nft_data = validated_data["data"]
            nft_user = validated_data["user"]

            project_id = settings.ONE_MODEL_PROJECT_ID
            url = settings.ONE_MODEL_URL

            nft = ImageNFT.objects.create(data=nft_data, user=nft_user)
            nft.save()

            r = requests.post(
                url,
                {
                    "project_id": project_id,
                    "data": nft_data,
                    "file_format": "png",
                    "callback_url": f"{urljoin(settings.CALLBACK_URL, str(nft.id))}/",
                },
            )

            if r.status_code == 201:
                return Response(
                    status=status.HTTP_201_CREATED,
                )
            else:
                return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, *args, **kwargs):
        partial = True
        instance = self.get_object()

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        self.perform_update(serializer)

        if settings.MINT:
            minter_url = settings.MINTER_URL

            # Minting
            res = requests.post(
                minter_url, {"imageURL": instance.image_url, "user": instance.user}
            )

            print(res.json())

        return Response(serializer.data)


def display_nft(request):
    nfts = ImageNFT.objects.filter(status=ImageNFT.GENERATED).order_by("-created_at")
    return render(request, "nft.html", {"nfts": nfts})
