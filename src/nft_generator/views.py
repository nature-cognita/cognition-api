# import csv
# from datetime import datetime
from io import StringIO
from urllib.parse import urljoin

import pandas as pd
import requests
from django.conf import settings

# from api.models import Location, Sensor, SensorRecord
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import GenerateNFTForm

# from django.utils.timezone import make_aware


def generate_nft(request):
    if request.method == "POST":
        form = GenerateNFTForm(request.POST)
        if form.is_valid():
            api_key = settings.NFT_GENERATOR_API_KEY
            sensor_name = settings.NFT_GENERATOR_SENSOR_NAME
            res = requests.get(
                f"https://www.irrimaxlive.com/api/?cmd=getreadings&key={api_key}&name={sensor_name}"
            )

            print(res.text)

            df = pd.read_csv(StringIO(res.text))

            df.drop("Date Time", inplace=True, axis=1)  # Removing date column
            df.drop(df[df["A1(5)"] < 0].index, inplace=True)  # Removing -1 rows

            host_url = settings.HOST_URL

            url = urljoin(host_url, "/api/nfts/")
            user = form.cleaned_data.get("user")
            data = df.to_string(index=False)

            res = requests.post(url, {"data": data, "user": user})

            return HttpResponseRedirect("/generator-success/")
    else:
        form = GenerateNFTForm()
    return render(request, "generator.html", {"form": form})


def generator_success(request):
    return render(request, "generator-success.html")
