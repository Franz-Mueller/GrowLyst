from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    # List (table) views – class-based
    path("plants/", views.PlantListView.as_view(), name="plants"),
    path("plantstages/", views.PlantstageListView.as_view(), name="plantstages"),
    path(
        "plantstagelogs/", views.PlantstagelogListView.as_view(), name="plantstagelogs"
    ),
    path("strains/", views.StrainListView.as_view(), name="strains"),
    path("breeders/", views.BreederListView.as_view(), name="breeders"),
    path("mediumtypes/", views.MediumtypeListView.as_view(), name="mediumtypes"),
    path("mediums/", views.MediumListView.as_view(), name="mediums"),
    path("gallery/", views.gallery, name="gallery"),
    path("grows/", views.GrowListView.as_view(), name="grows"),
    path("growtypes/", views.GrowtypeListView.as_view(), name="growtypes"),
    path("environments/", views.EnvironmentListView.as_view(), name="environments"),
    path("measurements/", views.MeasurementListView.as_view(), name="measurements"),
    path("units/", views.UnitListView.as_view(), name="units"),
    path("unittypes/", views.UnittypeListView.as_view(), name="unittypes"),
    path(
        "actioncategories/",
        views.ActioncategoryListView.as_view(),
        name="actioncategories",
    ),
    path("actiontypes/", views.ActiontypeListView.as_view(), name="actiontypes"),
    path("actionlogs/", views.ActionLogListView.as_view(), name="actionlogs"),
    path("nutrients/", views.NutrientListView.as_view(), name="nutrients"),
    path("nutritions/", views.NutritionListView.as_view(), name="nutritions"),
    path("groups/", views.GroupListView.as_view(), name="groups"),
    path(
        "measurementtypes/",
        views.MeasurementtypeListView.as_view(),
        name="measurementtypes",
    ),
    # Card/detail views (all class-based)
    path("plant/<int:plant_id>/", views.PlantDetailView.as_view(), name="plant"),
    path(
        "plantstage/<int:plantstage_id>/",
        views.PlantstageDetailView.as_view(),
        name="plantstage",
    ),
    path(
        "plantstagelog/<int:plantstagelog_id>/",
        views.PlantstagelogDetailView.as_view(),
        name="plantstagelog",
    ),
    path("strain/<int:strain_id>/", views.StrainDetailView.as_view(), name="strain"),
    path(
        "breeder/<int:breeder_id>/", views.BreederDetailView.as_view(), name="breeder"
    ),
    path(
        "mediumtype/<int:mediumtype_id>/",
        views.MediumtypeDetailView.as_view(),
        name="mediumtype",
    ),
    path("medium/<int:medium_id>/", views.MediumDetailView.as_view(), name="medium"),
    path(
        "plantphoto/<int:plantphoto_id>/",
        views.PlantphotoDetailView.as_view(),
        name="plantphoto",
    ),
    path("grow/<int:grow_id>/", views.GrowDetailView.as_view(), name="grow"),
    path(
        "growtype/<int:growtype_id>/",
        views.GrowtypeDetailView.as_view(),
        name="growtype",
    ),
    path(
        "environment/<int:environment_id>/",
        views.EnvironmentDetailView.as_view(),
        name="environment",
    ),
    path(
        "measurement/<int:measurement_id>/",
        views.MeasurementDetailView.as_view(),
        name="measurement",
    ),
    path("unit/<int:unit_id>/", views.UnitDetailView.as_view(), name="unit"),
    path(
        "unittype/<int:unittype_id>/",
        views.UnittypeDetailView.as_view(),
        name="unittype",
    ),
    path(
        "actioncategory/<int:actioncategory_id>/",
        views.ActioncategoryDetailView.as_view(),
        name="actioncategory",
    ),
    path(
        "actiontype/<int:actiontype_id>/",
        views.ActiontypeDetailView.as_view(),
        name="actiontype",
    ),
    path(
        "actionlog/<int:actionlog_id>/",
        views.ActionLogDetailView.as_view(),
        name="actionlog",
    ),
    path(
        "nutrient/<int:nutrient_id>/",
        views.NutrientDetailView.as_view(),
        name="nutrient",
    ),
    path(
        "nutrition/<int:nutrition_id>/",
        views.NutritionDetailView.as_view(),
        name="nutrition",
    ),
    path("group/<int:group_id>/", views.GroupDetailView.as_view(), name="group"),
    path(
        "measurementtype/<int:measurementtype_id>/",
        views.MeasurementtypeDetailView.as_view(),
        name="measurementtype",
    ),
    # Add (create) views
    path("plant/add/", views.PlantCreateView.as_view(), name="add_plant"),
    path(
        "plantstage/add/", views.PlantstageCreateView.as_view(), name="add_plantstage"
    ),
    path(
        "plantstagelog/add/",
        views.PlantstagelogCreateView.as_view(),
        name="add_plantstagelog",
    ),
    path("strain/add/", views.StrainCreateView.as_view(), name="add_strain"),
    path("breeder/add/", views.BreederCreateView.as_view(), name="add_breeder"),
    path(
        "mediumtype/add/", views.MediumtypeCreateView.as_view(), name="add_mediumtype"
    ),
    path("medium/add/", views.MediumCreateView.as_view(), name="add_medium"),
    path(
        "plantphoto/add/", views.PlantphotoCreateView.as_view(), name="add_plantphoto"
    ),
    path("grow/add/", views.GrowCreateView.as_view(), name="add_grow"),
    path("growtype/add/", views.GrowtypeCreateView.as_view(), name="add_growtype"),
    path(
        "environment/add/",
        views.EnvironmentCreateView.as_view(),
        name="add_environment",
    ),
    path(
        "measurement/add/",
        views.MeasurementCreateView.as_view(),
        name="add_measurement",
    ),
    path("unit/add/", views.UnitCreateView.as_view(), name="add_unit"),
    path("unittype/add/", views.UnittypeCreateView.as_view(), name="add_unittype"),
    path(
        "actioncategory/add/",
        views.ActioncategoryCreateView.as_view(),
        name="add_actioncategory",
    ),
    path(
        "actiontype/add/", views.ActiontypeCreateView.as_view(), name="add_actiontype"
    ),
    path("actionlog/add/", views.ActionLogCreateView.as_view(), name="add_actionlog"),
    path("nutrient/add/", views.NutrientCreateView.as_view(), name="add_nutrient"),
    path("nutrition/add/", views.NutritionCreateView.as_view(), name="add_nutrition"),
    path("group/add/", views.GroupCreateView.as_view(), name="add_group"),
    path(
        "measurementtype/add/",
        views.MeasurementtypeCreateView.as_view(),
        name="add_measurementtype",
    ),
    # Edit (update) views
    path("plant/<int:pk>/edit/", views.PlantUpdateView.as_view(), name="edit_plant"),
    path(
        "plantstage/<int:pk>/edit/",
        views.PlantstageUpdateView.as_view(),
        name="edit_plantstage",
    ),
    path(
        "plantstagelog/<int:pk>/edit/",
        views.PlantstagelogUpdateView.as_view(),
        name="edit_plantstagelog",
    ),
    path("strain/<int:pk>/edit/", views.StrainUpdateView.as_view(), name="edit_strain"),
    path(
        "breeder/<int:pk>/edit/", views.BreederUpdateView.as_view(), name="edit_breeder"
    ),
    path(
        "mediumtype/<int:pk>/edit/",
        views.MediumtypeUpdateView.as_view(),
        name="edit_mediumtype",
    ),
    path("medium/<int:pk>/edit/", views.MediumUpdateView.as_view(), name="edit_medium"),
    path(
        "plantphoto/<int:pk>/edit/",
        views.PlantphotoUpdateView.as_view(),
        name="edit_plantphoto",
    ),
    path("grow/<int:pk>/edit/", views.GrowUpdateView.as_view(), name="edit_grow"),
    path(
        "growtype/<int:pk>/edit/",
        views.GrowtypeUpdateView.as_view(),
        name="edit_growtype",
    ),
    path(
        "environment/<int:pk>/edit/",
        views.EnvironmentUpdateView.as_view(),
        name="edit_environment",
    ),
    path(
        "measurement/<int:pk>/edit/",
        views.MeasurementUpdateView.as_view(),
        name="edit_measurement",
    ),
    path("unit/<int:pk>/edit/", views.UnitUpdateView.as_view(), name="edit_unit"),
    path(
        "unittype/<int:pk>/edit/",
        views.UnittypeUpdateView.as_view(),
        name="edit_unittype",
    ),
    path(
        "actioncategory/<int:pk>/edit/",
        views.ActioncategoryUpdateView.as_view(),
        name="edit_actioncategory",
    ),
    path(
        "actiontype/<int:pk>/edit/",
        views.ActiontypeUpdateView.as_view(),
        name="edit_actiontype",
    ),
    path(
        "actionlog/<int:pk>/edit/",
        views.ActionLogUpdateView.as_view(),
        name="edit_actionlog",
    ),
    path(
        "nutrient/<int:pk>/edit/",
        views.NutrientUpdateView.as_view(),
        name="edit_nutrient",
    ),
    path(
        "nutrition/<int:pk>/edit/",
        views.NutritionUpdateView.as_view(),
        name="edit_nutrition",
    ),
    path("group/<int:pk>/edit/", views.GroupUpdateView.as_view(), name="edit_group"),
    path(
        "measurementtype/<int:pk>/edit/",
        views.MeasurementtypeUpdateView.as_view(),
        name="edit_measurementtype",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
