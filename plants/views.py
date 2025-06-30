from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required

from .models import Plant, Grow, Measurement, Environment, Group


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


@login_required
def grows(request):
    grows = Grow.objects.for_user(request.user)
    content = {"grows": grows, "section": "grows"}
    return render(request, "plants/grows.html", content)


@login_required
def grow(request, grow_id):
    grow = Grow.objects.get(id=grow_id)
    content = {"grow": grow}
    return render(request, "plants/grow.html", content)


@login_required
def environments(request):
    environments = Environment.objects.recent_for_user(request.user)
    content = {"environments": environments, "section": "environments"}
    return render(request, "plants/environments.html", content)


@login_required
def environment(request, environment_id):
    environment = Environment.objects.get(id=environment_id)
    content = {"environment": environment}
    return render(request, "plants/environment.html", content)


@login_required
def groups(request):
    groups = Group.objects.recent_for_user(request.user)
    content = {"groups": groups, "section": "groups"}
    return render(request, "plants/groups.html", content)


@login_required
def group(request, group_id):
    group = Group.objects.get(id=group_id)
    content = {"group": group}
    return render(request, "plants/group.html", content)
