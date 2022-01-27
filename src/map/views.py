from django.shortcuts import render


def display_map(request):
    return render(request, "map.html")
