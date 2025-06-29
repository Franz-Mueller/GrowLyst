from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required

from .models import Plant, Measurement


@login_required
def plants(request):
    plants = Plant.objects.for_user(request.user)
    content = {"plants": plants, "section": "plants"}
    return render(request, "plants/plants.html", content)


@login_required
def plant(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    measurements = Measurement.objects.filter(user=request.user, plant=plant)
    content = {"plant": plant, "measurements": measurements}
    return render(request, "plants/plant.html", content)
