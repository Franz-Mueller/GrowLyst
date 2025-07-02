from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from ..models import *


def get_display_fields(obj, exclude=None):
    if exclude is None:
        exclude = {"id", "created_at", "updated_at", "user", "profile_image", "image"}
    return [
        field
        for field in obj._meta.get_fields()
        if getattr(field, "attname", None) not in exclude
        and not field.auto_created
        and field.concrete
    ]


class PlantDetailView(LoginRequiredMixin, DetailView):
    model = Plant
    template_name = "card.html"
    context_object_name = "object"
    pk_url_kwarg = "plant_id"
    edit_url_name = "edit_plant"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["display_fields"] = get_display_fields(self.object)
        context["edit_url_name"] = self.edit_url_name

        context["user_name"] = (
            self.request.user.username
            if self.request.user.is_authenticated
            else "Guest"
        )
        return context


class PlantstageDetailView(LoginRequiredMixin, DetailView):
    model = Plantstage
    template_name = "card.html"
    context_object_name = "object"
    pk_url_kwarg = "plantstage_id"
    edit_url_name = "edit_plantstage"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["display_fields"] = get_display_fields(self.object)
        context["edit_url_name"] = self.edit_url_name

        context["user_name"] = (
            self.request.user.username
            if self.request.user.is_authenticated
            else "Guest"
        )
        return context


class PlantstagelogDetailView(LoginRequiredMixin, DetailView):
    model = Plantstagelog
    template_name = "card.html"
    context_object_name = "object"
    pk_url_kwarg = "plantstagelog_id"
    edit_url_name = "edit_plantstagelog"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["display_fields"] = get_display_fields(self.object)
        context["edit_url_name"] = self.edit_url_name

        context["user_name"] = (
            self.request.user.username
            if self.request.user.is_authenticated
            else "Guest"
        )
        return context


class StrainDetailView(LoginRequiredMixin, DetailView):
    model = Strain
    template_name = "card.html"
    context_object_name = "object"
    pk_url_kwarg = "strain_id"
    edit_url_name = "edit_strain"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["display_fields"] = get_display_fields(self.object)
        context["edit_url_name"] = self.edit_url_name

        context["user_name"] = (
            self.request.user.username
            if self.request.user.is_authenticated
            else "Guest"
        )
        return context


class BreederDetailView(LoginRequiredMixin, DetailView):
    model = Breeder
    template_name = "card.html"
    context_object_name = "object"
    pk_url_kwarg = "breeder_id"
    edit_url_name = "edit_breeder"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["display_fields"] = get_display_fields(self.object)
        context["edit_url_name"] = self.edit_url_name

        context["user_name"] = (
            self.request.user.username
            if self.request.user.is_authenticated
            else "Guest"
        )
        return context


class MediumtypeDetailView(LoginRequiredMixin, DetailView):
    model = Mediumtype
    template_name = "card.html"
    context_object_name = "object"
    pk_url_kwarg = "mediumtype_id"
    edit_url_name = "edit_mediumtype"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["display_fields"] = get_display_fields(self.object)
        context["edit_url_name"] = self.edit_url_name

        context["user_name"] = (
            self.request.user.username
            if self.request.user.is_authenticated
            else "Guest"
        )
        return context


class MediumDetailView(LoginRequiredMixin, DetailView):
    model = Medium
    template_name = "card.html"
    context_object_name = "object"
    pk_url_kwarg = "medium_id"
    edit_url_name = "edit_medium"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["display_fields"] = get_display_fields(self.object)
        context["edit_url_name"] = self.edit_url_name

        context["user_name"] = (
            self.request.user.username
            if self.request.user.is_authenticated
            else "Guest"
        )
        return context


class PlantphotoDetailView(LoginRequiredMixin, DetailView):
    model = Plantphoto
    template_name = "card.html"
    context_object_name = "object"
    pk_url_kwarg = "plantphoto_id"
    edit_url_name = "edit_plantphoto"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["display_fields"] = get_display_fields(self.object)
        context["edit_url_name"] = self.edit_url_name

        context["user_name"] = (
            self.request.user.username
            if self.request.user.is_authenticated
            else "Guest"
        )
        return context


class GrowDetailView(LoginRequiredMixin, DetailView):
    model = Grow
    template_name = "card.html"
    context_object_name = "object"
    pk_url_kwarg = "grow_id"
    edit_url_name = "edit_grow"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["display_fields"] = get_display_fields(self.object)
        context["edit_url_name"] = self.edit_url_name

        context["user_name"] = (
            self.request.user.username
            if self.request.user.is_authenticated
            else "Guest"
        )
        return context


class GrowtypeDetailView(LoginRequiredMixin, DetailView):
    model = Growtype
    template_name = "card.html"
    context_object_name = "object"
    pk_url_kwarg = "growtype_id"
    edit_url_name = "edit_growtype"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["display_fields"] = get_display_fields(self.object)
        context["edit_url_name"] = self.edit_url_name

        context["user_name"] = (
            self.request.user.username
            if self.request.user.is_authenticated
            else "Guest"
        )
        return context


class EnvironmentDetailView(LoginRequiredMixin, DetailView):
    model = Environment
    template_name = "card.html"
    context_object_name = "object"
    pk_url_kwarg = "environment_id"
    edit_url_name = "edit_environment"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["display_fields"] = get_display_fields(self.object)
        context["edit_url_name"] = self.edit_url_name

        context["user_name"] = (
            self.request.user.username
            if self.request.user.is_authenticated
            else "Guest"
        )
        return context


class MeasurementDetailView(LoginRequiredMixin, DetailView):
    model = Measurement
    template_name = "card.html"
    context_object_name = "object"
    pk_url_kwarg = "measurement_id"
    edit_url_name = "edit_measurement"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["display_fields"] = get_display_fields(self.object)
        context["edit_url_name"] = self.edit_url_name

        context["user_name"] = (
            self.request.user.username
            if self.request.user.is_authenticated
            else "Guest"
        )
        return context


class UnitDetailView(LoginRequiredMixin, DetailView):
    model = Unit
    template_name = "card.html"
    context_object_name = "object"
    pk_url_kwarg = "unit_id"
    edit_url_name = "edit_unit"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["display_fields"] = get_display_fields(self.object)
        context["edit_url_name"] = self.edit_url_name

        context["user_name"] = (
            self.request.user.username
            if self.request.user.is_authenticated
            else "Guest"
        )
        return context


class UnittypeDetailView(LoginRequiredMixin, DetailView):
    model = Unittype
    template_name = "card.html"
    context_object_name = "object"
    pk_url_kwarg = "unittype_id"
    edit_url_name = "edit_unittype"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["display_fields"] = get_display_fields(self.object)
        context["edit_url_name"] = self.edit_url_name

        context["user_name"] = (
            self.request.user.username
            if self.request.user.is_authenticated
            else "Guest"
        )
        return context


class ActioncategoryDetailView(LoginRequiredMixin, DetailView):
    model = Actioncategory
    template_name = "card.html"
    context_object_name = "object"
    pk_url_kwarg = "actioncategory_id"
    edit_url_name = "edit_actioncategory"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["display_fields"] = get_display_fields(self.object)
        context["edit_url_name"] = self.edit_url_name

        context["user_name"] = (
            self.request.user.username
            if self.request.user.is_authenticated
            else "Guest"
        )
        return context


class ActiontypeDetailView(LoginRequiredMixin, DetailView):
    model = Actiontype
    template_name = "card.html"
    context_object_name = "object"
    pk_url_kwarg = "actiontype_id"
    edit_url_name = "edit_actiontype"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["display_fields"] = get_display_fields(self.object)
        context["edit_url_name"] = self.edit_url_name

        context["user_name"] = (
            self.request.user.username
            if self.request.user.is_authenticated
            else "Guest"
        )
        return context


class ActionLogDetailView(LoginRequiredMixin, DetailView):
    model = ActionLog
    template_name = "card.html"
    context_object_name = "object"
    pk_url_kwarg = "actionlog_id"
    edit_url_name = "edit_actionlog"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["display_fields"] = get_display_fields(self.object)
        context["edit_url_name"] = self.edit_url_name

        context["user_name"] = (
            self.request.user.username
            if self.request.user.is_authenticated
            else "Guest"
        )
        return context


class NutrientDetailView(LoginRequiredMixin, DetailView):
    model = Nutrient
    template_name = "card.html"
    context_object_name = "object"
    pk_url_kwarg = "nutrient_id"
    edit_url_name = "edit_nutrient"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["display_fields"] = get_display_fields(self.object)
        context["edit_url_name"] = self.edit_url_name

        context["user_name"] = (
            self.request.user.username
            if self.request.user.is_authenticated
            else "Guest"
        )
        return context


class NutritionDetailView(LoginRequiredMixin, DetailView):
    model = Nutrition
    template_name = "card.html"
    context_object_name = "object"
    pk_url_kwarg = "nutrition_id"
    edit_url_name = "edit_nutrition"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["display_fields"] = get_display_fields(self.object)
        context["edit_url_name"] = self.edit_url_name

        context["user_name"] = (
            self.request.user.username
            if self.request.user.is_authenticated
            else "Guest"
        )
        return context


class GroupDetailView(LoginRequiredMixin, DetailView):
    model = Group
    template_name = "card.html"
    context_object_name = "object"
    pk_url_kwarg = "group_id"
    edit_url_name = "edit_group"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["display_fields"] = get_display_fields(self.object)
        context["edit_url_name"] = self.edit_url_name

        context["user_name"] = (
            self.request.user.username
            if self.request.user.is_authenticated
            else "Guest"
        )
        return context


class MeasurementtypeDetailView(LoginRequiredMixin, DetailView):
    model = Measurementtype
    template_name = "card.html"
    context_object_name = "object"
    pk_url_kwarg = "measurementtype_id"
    edit_url_name = "edit_measurementtype"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["display_fields"] = get_display_fields(self.object)
        context["edit_url_name"] = self.edit_url_name

        context["user_name"] = (
            self.request.user.username
            if self.request.user.is_authenticated
            else "Guest"
        )
        return context
