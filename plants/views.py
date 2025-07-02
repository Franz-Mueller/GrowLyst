from django.shortcuts import render, redirect, get_object_or_404
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
