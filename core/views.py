from django.shortcuts import render
from plants.models import Plant, Grow


def index(request):
    if request.user.is_authenticated:
        content = {"user_name": request.user.username}
        return render(request, "core/dashboard.html", content)
    else:
        return render(request, "core/index.html")
