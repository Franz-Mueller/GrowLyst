from django.urls import path

from . import views

urlpatterns = [
    path("plants/", views.plants, name="plants"),
    path("plant/<int:plant_id>/", views.plant, name="plant"),
]
