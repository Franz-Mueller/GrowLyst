from django.urls import path

from . import views

urlpatterns = [
    path("plants/", views.plants, name="plants"),
    path("plant/<int:plant_id>/", views.plant, name="plant"),
    path("grows/", views.grows, name="grows"),
    path("grow/<int:grow_id>/", views.grow, name="grow"),
    path("environments/", views.environments, name="environments"),
    path("environment/<int:environment_id>/", views.environment, name="environment"),
    path("groups/", views.groups, name="groups"),
    path("group/<int:group_id>/", views.group, name="group"),
]
