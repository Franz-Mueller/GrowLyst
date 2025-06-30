from django.shortcuts import render
from plants.models import Plant, Grow


def index(request):
    if request.user.is_authenticated:
        plants = Plant.objects.recent_for_user(request.user)
        grows = Grow.objects.recent_for_user(request.user, limit=3)
        content = {"plants": plants, "grows": grows, "section": "dashboard"}
        return render(request, "core/dashboard.html", content)
    else:
        return render(request, "core/index.html")
