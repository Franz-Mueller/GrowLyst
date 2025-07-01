from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from ..models import *


class TableListView(LoginRequiredMixin, ListView):
    template_name = "table.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        model = self.model
        fields = self.table_fields or [f.name for f in model._meta.fields]
        rows = self.get_queryset().values("id", *fields)
        context["fields"] = fields
        context["rows"] = rows
        context["headers"] = self.table_captions
        context["model_verbose"] = model._meta.verbose_name_plural.title()
        context["image_fields"] = getattr(self, "image_fields", [])
        context["page_url"] = self.page_url
        context["add_url_name"] = self.add_url_name
        return context


# ---- LIST VIEWS ----


class PlantListView(TableListView):
    model = Plant
    table_captions = [
        "Image",
        "Name",
        "Strain",
        "Environment",
        "Grow",
        "Group",
        "Medium",
        "Created At",
        "Updated At",
    ]
    table_fields = [
        "profile_image",
        "name",
        "strain__name",
        "environment__name",
        "grow__name",
        "group__name",
        "medium__name",
        "created_at",
        "updated_at",
    ]
    image_fields = ["profile_image"]
    page_url = "plant"
    add_url_name = "add_plant"


class PlantstageListView(TableListView):
    model = Plantstage
    table_captions = ["Name", "Description", "Created At", "Updated At"]
    table_fields = ["name", "description", "created_at", "updated_at"]
    image_fields = []
    page_url = "plantstage"
    add_url_name = "add_plantstage"


class PlantstagelogListView(TableListView):
    model = Plantstagelog
    table_captions = [
        "Plant",
        "Plantstage",
        "Date of Change",
        "Created At",
        "Updated At",
    ]
    table_fields = [
        "plant__name",
        "plantstage__name",
        "date_of_change",
        "created_at",
        "updated_at",
    ]
    image_fields = []
    page_url = "plantstagelog"
    add_url_name = "add_plantstagelog"


class StrainListView(TableListView):
    model = Strain
    table_captions = ["Name", "Description", "Breeder", "Created At", "Updated At"]
    table_fields = ["name", "description", "breeder__name", "created_at", "updated_at"]
    image_fields = []
    page_url = "strain"
    add_url_name = "add_strain"


class BreederListView(TableListView):
    model = Breeder
    table_captions = ["Name", "Description", "Website", "Created At", "Updated At"]
    table_fields = ["name", "description", "website", "created_at", "updated_at"]
    image_fields = []
    page_url = "breeder"
    add_url_name = "add_breeder"


class MediumtypeListView(TableListView):
    model = Mediumtype
    table_captions = ["Name", "Description", "Created At", "Updated At"]
    table_fields = ["name", "description", "created_at", "updated_at"]
    image_fields = []
    page_url = "mediumtype"
    add_url_name = "add_mediumtype"


class MediumListView(TableListView):
    model = Medium
    table_captions = ["Name", "Description", "Medium Type", "Created At", "Updated At"]
    table_fields = [
        "name",
        "description",
        "medium_type__name",
        "created_at",
        "updated_at",
    ]
    image_fields = []
    page_url = "medium"
    add_url_name = "add_medium"


class PlantphotoListView(TableListView):
    model = Plantphoto
    table_captions = ["Image", "Plant", "Description", "Created At", "Updated At"]
    table_fields = ["image", "plant__name", "description", "created_at", "updated_at"]
    image_fields = ["image"]
    page_url = "plantphoto"
    add_url_name = "add_plantphoto"


class GrowListView(TableListView):
    model = Grow
    table_captions = ["Name", "Type", "Description", "Created At", "Updated At"]
    table_fields = ["name", "type__name", "description", "created_at", "updated_at"]
    image_fields = []
    page_url = "grow"
    add_url_name = "add_grow"


class GrowtypeListView(TableListView):
    model = Growtype
    table_captions = ["Name", "Description", "Created At", "Updated At"]
    table_fields = ["name", "description", "created_at", "updated_at"]
    image_fields = []
    page_url = "growtype"
    add_url_name = "add_growtype"


class EnvironmentListView(TableListView):
    model = Environment
    table_captions = ["Name", "Description", "Created At", "Updated At"]
    table_fields = ["name", "description", "created_at", "updated_at"]
    image_fields = []
    page_url = "environment"
    add_url_name = "add_environment"


class MeasurementListView(TableListView):
    model = Measurement
    table_captions = [
        "Grow",
        "Environment",
        "Plant",
        "Type",
        "Value",
        "Unit",
        "Created At",
        "Updated At",
    ]
    table_fields = [
        "grow__name",
        "environment__name",
        "plant__name",
        "measurementtype__name",
        "value",
        "unit__symbol",
        "created_at",
        "updated_at",
    ]
    image_fields = []
    page_url = "measurement"
    add_url_name = "add_measurement"


class UnitListView(TableListView):
    model = Unit
    table_captions = [
        "Name",
        "Symbol",
        "Conversion Factor to Base",
        "Created At",
        "Updated At",
    ]
    table_fields = [
        "name",
        "symbol",
        "conversion_factor_to_base",
        "created_at",
        "updated_at",
    ]
    image_fields = []
    page_url = "unit"
    add_url_name = "add_unit"


class UnittypeListView(TableListView):
    model = Unittype
    table_captions = ["Name", "Description", "Base Unit", "Created At", "Updated At"]
    table_fields = ["name", "description", "baseunit__name", "created_at", "updated_at"]
    image_fields = []
    page_url = "unittype"
    add_url_name = "add_unittype"


class ActioncategoryListView(TableListView):
    model = Actioncategory
    table_captions = ["Name", "Description", "Created At", "Updated At"]
    table_fields = ["name", "description", "created_at", "updated_at"]
    image_fields = []
    page_url = "actioncategory"
    add_url_name = "add_actioncategory"


class ActiontypeListView(TableListView):
    model = Actiontype
    table_captions = ["Name", "Description", "Category", "Created At", "Updated At"]
    table_fields = ["name", "description", "category__name", "created_at", "updated_at"]
    image_fields = []
    page_url = "actiontype"
    add_url_name = "add_actiontype"


class ActionLogListView(TableListView):
    model = ActionLog
    table_captions = [
        "Grow",
        "Environment",
        "Plant",
        "Category",
        "Action Type",
        "Description",
        "Created At",
        "Updated At",
    ]
    table_fields = [
        "grow__name",
        "environment__name",
        "plant__name",
        "Actioncategory__name",
        "action_type__name",
        "description",
        "created_at",
        "updated_at",
    ]
    image_fields = []
    page_url = "actionlog"
    add_url_name = "add_actionlog"


class NutrientListView(TableListView):
    model = Nutrient
    table_captions = [
        "Name",
        "Description",
        "Producer",
        "URL",
        "Created At",
        "Updated At",
    ]
    table_fields = [
        "name",
        "description",
        "producer",
        "url",
        "created_at",
        "updated_at",
    ]
    image_fields = []
    page_url = "nutrient"
    add_url_name = "add_nutrient"


class NutritionListView(TableListView):
    model = Nutrition
    table_captions = [
        "Action Log",
        "Nutrient",
        "Amount",
        "Unit",
        "Created At",
        "Updated At",
    ]
    table_fields = [
        "actionlog__id",
        "nutrient__name",
        "amount",
        "unit__symbol",
        "created_at",
        "updated_at",
    ]
    image_fields = []
    page_url = "nutrition"
    add_url_name = "add_nutrition"


class GroupListView(TableListView):
    model = Group
    table_captions = ["Name", "Description", "Created At", "Updated At"]
    table_fields = ["name", "description", "created_at", "updated_at"]
    image_fields = []
    page_url = "group"
    add_url_name = "add_group"


class MeasurementtypeListView(TableListView):
    model = Measurementtype
    table_captions = ["Name", "Description", "Unit Type"]
    table_fields = ["name", "description", "unittype__name"]
    image_fields = []
    page_url = "measurementtype"
    add_url_name = "add_measurementtype"
