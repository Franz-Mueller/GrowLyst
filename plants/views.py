import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .extra_views.table_views import *
from .models import *
from .forms import PlantForm
from .extra_views.card_views import *
from .extra_views.add_update_views import *


@login_required
def gallery(request):
    plantphotos = Plantphoto.objects.for_user_ordered_by_created_at(request.user)
    content = {
        "rows": plantphotos,
        "add_url_name": "add_plantphoto",
        "section": "gallery",
    }
    return render(request, "plants/gallery.html", content)


@login_required
def progress_stage(request, plant_id):
    plant = Plant.objects.get(id=plant_id, user=request.user)
    stages = Plantstage.objects.all().order_by("order")
    this_is_next = False
    for stage in stages:
        if this_is_next:
            plant.current_stage = stage
            plantstagelog = Plantstagelog.objects.create(
                user=request.user,
                plant=plant,
                plantstage=stage,
                date_of_change=datetime.date.today(),
            )
            plantstagelog.save()
            plant.save()
            return HttpResponseRedirect(reverse("plant", kwargs={"plant_id": plant_id}))
        if stage == plant.current_stage:
            this_is_next = True
    return HttpResponseRedirect(reverse("plant", kwargs={"plant_id": plant_id}))
