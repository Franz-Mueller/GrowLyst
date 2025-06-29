from django.shortcuts import render
from plants.models import Plant


def index(request):
    if request.user.is_authenticated:
        plants = Plant.objects.recent_for_user(request.user)
        content = {"plants": plants, "section": "dashboard"}
        return render(request, "core/dashboard.html", content)
    else:
        return render(request, "core/index.html")
