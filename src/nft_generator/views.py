# import csv
# from datetime import datetime
from datetime import datetime
from io import StringIO
from urllib.parse import urljoin

import pandas as pd
import requests
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import GenerateNFTForm

# from django.utils.timezone import make_aware


def get_last_hour():
    now = datetime.now()
    return now.strftime("%Y%m%d%H0000")


def generate_nft(request):
    if request.method == "POST":
        form = GenerateNFTForm(request.POST)
        if form.is_valid():
            api_key = settings.NFT_GENERATOR_API_KEY
            sensor_name = settings.NFT_GENERATOR_SENSOR_NAME
            from_date = get_last_hour()

            res = requests.get(
                f"https://www.irrimaxlive.com/api/?cmd=getreadings&key={api_key}&name={sensor_name}&from={from_date}"
            )

            print("External API Data")
            print(res.text)

            df = pd.read_csv(StringIO(res.text))

            df.drop("Date Time", inplace=True, axis=1)  # Removing date column
            df.drop(df[df["A1(5)"] < 0].index, inplace=True)  # Removing -1 rows

            last_row = df.iloc[-1:]

            # df.to_csv("test.csv", index=False)

            host_url = settings.HOST_URL

            url = urljoin(host_url, "/api/nfts/")
            user = form.cleaned_data.get("user")
            data = last_row.to_csv(index=False)

            print("Cleanup for generation")
            print(data)

            res = requests.post(url, {"data": data, "user": user})

            return HttpResponseRedirect("/generator-success/")
    else:
        form = GenerateNFTForm()
    return render(request, "generator.html", {"form": form})


def generator_success(request):
    return render(request, "generator-success.html")
