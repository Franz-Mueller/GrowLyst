from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required

from .models import Plant


@login_required
def plants(request):
    users_plant_list = Plant.objects.filter(user=request.user)
    context = {"users_plant_list": users_plant_list}
    return render(request, "plants/plants.html", context)


@login_required
def plant(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    context = {"plant": plant}
    return render(request, "plants/plant.html", context)
