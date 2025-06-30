from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required

from .models import *


@login_required
def plants(request):
    """User Specific"""
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
    """User Specific"""
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
    """User Specific"""
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
    """User Specific"""
    groups = Group.objects.recent_for_user(request.user)
    content = {"groups": groups, "section": "groups"}
    return render(request, "plants/groups.html", content)


@login_required
def group(request, group_id):
    group = Group.objects.get(id=group_id)
    content = {"group": group}
    return render(request, "plants/group.html", content)


@login_required
def plantstages(request):
    """User Specific + Global"""
    plantstages = Plantstage.objects.for_user_and_global(request.user)
    content = {"plantstages": plantstages, "section": "plantstages"}
    return render(request, "plants/plantstages.html", content)


@login_required
def plantstage(request, plantstage_id):
    plantstage = Plantstage.objects.get(id=plantstage_id)
    content = {"plantstage": plantstage}
    return render(request, "plants/plantstage.html", content)


@login_required
def plantstagelogs(request):
    """User Specific"""
    plantstagelogs = Plantstagelog.objects.for_user(request.user)
    content = {"plantstagelogs": plantstagelogs, "section": "plantstagelogs"}
    return render(request, "plants/plantstagelogs.html", content)


@login_required
def plantstagelog(request, plantstagelog_id):
    plantstagelog = Plantstagelog.objects.get(id=plantstagelog_id)
    content = {"plantstagelog": plantstagelog}
    return render(request, "plants/plantstagelog.html", content)


@login_required
def strains(request):
    """User Specific + Global"""
    strains = Strain.objects.for_user_and_global(request.user)
    content = {"strains": strains, "section": "strains"}
    return render(request, "plants/strains.html", content)


@login_required
def strain(request, strain_id):
    strain = Strain.objects.get(id=strain_id)
    content = {"strain": strain}
    return render(request, "plants/strain.html", content)


@login_required
def breeders(request):
    """User Specific + Global"""
    breeders = Breeder.objects.for_user_and_global(request.user)
    content = {"breeders": breeders, "section": "breeders"}
    return render(request, "plants/breeders.html", content)


@login_required
def breeder(request, breeder_id):
    breeder = Breeder.objects.get(id=breeder_id)
    content = {"breeder": breeder}
    return render(request, "plants/breeder.html", content)


@login_required
def mediumtypes(request):
    """User Specific + Global"""
    mediumtypes = Mediumtype.objects.for_user_and_global(request.user)
    content = {"mediumtypes": mediumtypes, "section": "mediumtypes"}
    return render(request, "plants/mediumtypes.html", content)


@login_required
def mediumtype(request, mediumtype_id):
    mediumtype = Mediumtype.objects.get(id=mediumtype_id)
    content = {"mediumtype": mediumtype}
    return render(request, "plants/mediumtype.html", content)


@login_required
def media(request):
    """User Specific + Global"""
    media = Medium.objects.for_user_and_global(request.user)
    content = {"media": media, "section": "media"}
    return render(request, "plants/media.html", content)


@login_required
def medium(request, medium_id):
    medium = Medium.objects.get(id=medium_id)
    content = {"medium": medium}
    return render(request, "plants/medium.html", content)


@login_required
def plantphotos(request):
    """User Specific"""
    plantphotos = Plantphoto.objects.for_user(request.user)
    content = {"plantphotos": plantphotos, "section": "plantphotos"}
    return render(request, "plants/plantphotos.html", content)


@login_required
def plantphoto(request, plantphoto_id):
    plantphoto = Plantphoto.objects.get(id=plantphoto_id)
    content = {"plantphoto": plantphoto}
    return render(request, "plants/plantphoto.html", content)


@login_required
def growtypes(request):
    """User Specific"""
    growtypes = Growtype.objects.for_user(request.user)
    content = {"growtypes": growtypes, "section": "growtypes"}
    return render(request, "plants/growtypes.html", content)


@login_required
def growtype(request, growtype_id):
    growtype = Growtype.objects.get(id=growtype_id)
    content = {"growtype": growtype}
    return render(request, "plants/growtype.html", content)


@login_required
def measurements(request):
    """User Specific"""
    measurements = Measurement.objects.for_user(request.user)
    content = {"measurements": measurements, "section": "measurements"}
    return render(request, "plants/measurements.html", content)


@login_required
def measurement(request, measurement_id):
    measurement = Measurement.objects.get(id=measurement_id)
    content = {"measurement": measurement}
    return render(request, "plants/measurement.html", content)


@login_required
def units(request):
    """User Specific + Global"""
    units = Unit.objects.for_user_and_global(request.user)
    content = {"units": units, "section": "units"}
    return render(request, "plants/units.html", content)


@login_required
def unit(request, unit_id):
    unit = Unit.objects.get(id=unit_id)
    content = {"unit": unit}
    return render(request, "plants/unit.html", content)


@login_required
def unittypes(request):
    """User Specific + Global"""
    unittypes = Unittype.objects.for_user_and_global(request.user)
    content = {"unittypes": unittypes, "section": "unittypes"}
    return render(request, "plants/unittypes.html", content)


@login_required
def unittype(request, unittype_id):
    unittype = Unittype.objects.get(id=unittype_id)
    content = {"unittype": unittype}
    return render(request, "plants/unittype.html", content)


@login_required
def actioncategories(request):
    """User Specific + Global"""
    actioncategories = Actioncategory.objects.for_user_and_global(request.user)
    content = {"actioncategories": actioncategories, "section": "actioncategories"}
    return render(request, "plants/actioncategories.html", content)


@login_required
def actioncategory(request, actioncategory_id):
    actioncategory = Actioncategory.objects.get(id=actioncategory_id)
    content = {"actioncategory": actioncategory}
    return render(request, "plants/actioncategory.html", content)


@login_required
def actiontypes(request):
    """User Specific + Global"""
    actiontypes = Actiontype.objects.for_user_and_global(request.user)
    content = {"actiontypes": actiontypes, "section": "actiontypes"}
    return render(request, "plants/actiontypes.html", content)


@login_required
def actiontype(request, actiontype_id):
    actiontype = Actiontype.objects.get(id=actiontype_id)
    content = {"actiontype": actiontype}
    return render(request, "plants/actiontype.html", content)


@login_required
def actionlogs(request):
    """User Specific"""
    actionlogs = ActionLog.objects.for_user(request.user)
    content = {"actionlogs": actionlogs, "section": "actionlogs"}
    return render(request, "plants/actionlogs.html", content)


@login_required
def actionlog(request, actionlog_id):
    actionlog = ActionLog.objects.get(id=actionlog_id)
    content = {"actionlog": actionlog}
    return render(request, "plants/actionlog.html", content)


@login_required
def nutrients(request):
    """User Specific + Global"""
    nutrients = Nutrient.objects.for_user_and_global(request.user)
    content = {"nutrients": nutrients, "section": "nutrients"}
    return render(request, "plants/nutrients.html", content)


@login_required
def nutrient(request, nutrient_id):
    nutrient = Nutrient.objects.get(id=nutrient_id)
    content = {"nutrient": nutrient}
    return render(request, "plants/nutrient.html", content)


@login_required
def nutritions(request):
    """User Specific"""
    nutritions = Nutrition.objects.for_user(request.user)
    content = {"nutritions": nutritions, "section": "nutritions"}
    return render(request, "plants/nutritions.html", content)


@login_required
def nutrition(request, nutrition_id):
    nutrition = Nutrition.objects.get(id=nutrition_id)
    content = {"nutrition": nutrition}
    return render(request, "plants/nutrition.html", content)


@login_required
def measurementtypes(request):
    """User Specific + Global"""
    measurementtypes = Measurementtype.objects.for_user_and_global(request.user)
    content = {"measurementtypes": measurementtypes, "section": "measurementtypes"}
    return render(request, "plants/measurementtypes.html", content)


@login_required
def measurementtype(request, measurementtype_id):
    measurementtype = Measurementtype.objects.get(id=measurementtype_id)
    content = {"measurementtype": measurementtype}
    return render(request, "plants/measurementtype.html", content)
