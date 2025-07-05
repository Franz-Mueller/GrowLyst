# plants/views_forms.py (example name)

from django.urls import reverse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView

from ..models import *
from ..forms import *


# --- PLANT ---
class PlantCreateView(LoginRequiredMixin, CreateView):
    model = Plant
    form_class = PlantForm
    template_name = "form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("plant", kwargs={"plant_id": self.object.pk})


class PlantUpdateView(LoginRequiredMixin, UpdateView):
    model = Plant
    form_class = PlantForm
    template_name = "form.html"

    def get_queryset(self):
        return Plant.objects.filter(user=self.request.user)

    def get_success_url(self):
        return reverse("plant", kwargs={"plant_id": self.object.pk})


# --- PLANTSTAGE ---
class PlantstageCreateView(LoginRequiredMixin, CreateView):
    model = Plantstage
    form_class = PlantstageForm
    template_name = "form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("plantstage", kwargs={"plantstage_id": self.object.pk})


class PlantstageUpdateView(LoginRequiredMixin, UpdateView):
    model = Plantstage
    form_class = PlantstageForm
    template_name = "form.html"

    def get_queryset(self):
        return Plantstage.objects.filter(user=self.request.user)

    def get_success_url(self):
        return reverse("plantstage", kwargs={"plantstage_id": self.object.pk})


# --- PLANTSTAGELOG ---
class PlantstagelogCreateView(LoginRequiredMixin, CreateView):
    model = Plantstagelog
    form_class = PlantstagelogForm
    template_name = "form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("plantstagelog", kwargs={"plantstagelog_id": self.object.pk})


class PlantstagelogUpdateView(LoginRequiredMixin, UpdateView):
    model = Plantstagelog
    form_class = PlantstagelogForm
    template_name = "form.html"

    def get_queryset(self):
        return Plantstagelog.objects.filter(user=self.request.user)

    def get_success_url(self):
        return reverse("plantstagelog", kwargs={"plantstagelog_id": self.object.pk})


# --- STRAIN ---
class StrainCreateView(LoginRequiredMixin, CreateView):
    model = Strain
    form_class = StrainForm
    template_name = "form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("strain", kwargs={"strain_id": self.object.pk})


class StrainUpdateView(LoginRequiredMixin, UpdateView):
    model = Strain
    form_class = StrainForm
    template_name = "form.html"

    def get_queryset(self):
        return Strain.objects.filter(user=self.request.user)

    def get_success_url(self):
        return reverse("strain", kwargs={"strain_id": self.object.pk})


# --- BREEDER ---
class BreederCreateView(LoginRequiredMixin, CreateView):
    model = Breeder
    form_class = BreederForm
    template_name = "form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("breeder", kwargs={"breeder_id": self.object.pk})


class BreederUpdateView(LoginRequiredMixin, UpdateView):
    model = Breeder
    form_class = BreederForm
    template_name = "form.html"

    def get_queryset(self):
        return Breeder.objects.filter(user=self.request.user)

    def get_success_url(self):
        return reverse("breeder", kwargs={"breeder_id": self.object.pk})


# --- MEDIUMTYPE ---
class MediumtypeCreateView(LoginRequiredMixin, CreateView):
    model = Mediumtype
    form_class = MediumtypeForm
    template_name = "form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("mediumtype", kwargs={"mediumtype_id": self.object.pk})


class MediumtypeUpdateView(LoginRequiredMixin, UpdateView):
    model = Mediumtype
    form_class = MediumtypeForm
    template_name = "form.html"

    def get_queryset(self):
        return Mediumtype.objects.filter(user=self.request.user)

    def get_success_url(self):
        return reverse("mediumtype", kwargs={"mediumtype_id": self.object.pk})


# --- MEDIUM ---
class MediumCreateView(LoginRequiredMixin, CreateView):
    model = Medium
    form_class = MediumForm
    template_name = "form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("medium", kwargs={"mdeium_id": self.object.pk})


class MediumUpdateView(LoginRequiredMixin, UpdateView):
    model = Medium
    form_class = MediumForm
    template_name = "form.html"

    def get_queryset(self):
        return Medium.objects.filter(user=self.request.user)

    def get_success_url(self):
        return reverse("medium", kwargs={"mdeium_id": self.object.pk})


# --- PLANTPHOTO ---
class PlantphotoCreateView(LoginRequiredMixin, CreateView):
    model = Plantphoto
    form_class = PlantphotoForm
    template_name = "form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("plantphoto", kwargs={"plantphoto_id": self.object.pk})


class PlantphotoUpdateView(LoginRequiredMixin, UpdateView):
    model = Plantphoto
    form_class = PlantphotoForm
    template_name = "form.html"

    def get_queryset(self):
        return Plantphoto.objects.filter(user=self.request.user)

    def get_success_url(self):
        return reverse("plantphoto", kwargs={"plantphoto_id": self.object.pk})


# --- GROW ---
class GrowCreateView(LoginRequiredMixin, CreateView):
    model = Grow
    form_class = GrowForm
    template_name = "form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("grow", kwargs={"grow_id": self.object.pk})


class GrowUpdateView(LoginRequiredMixin, UpdateView):
    model = Grow
    form_class = GrowForm
    template_name = "form.html"

    def get_queryset(self):
        return Grow.objects.filter(user=self.request.user)

    def get_success_url(self):
        return reverse("grow", kwargs={"grow_id": self.object.pk})


# --- GROWTYPE ---
class GrowtypeCreateView(LoginRequiredMixin, CreateView):
    model = Growtype
    form_class = GrowtypeForm
    template_name = "form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("growtype", kwargs={"growtype_id": self.object.pk})


class GrowtypeUpdateView(LoginRequiredMixin, UpdateView):
    model = Growtype
    form_class = GrowtypeForm
    template_name = "form.html"

    def get_queryset(self):
        return Growtype.objects.filter(user=self.request.user)

    def get_success_url(self):
        return reverse("growtype", kwargs={"growtype_id": self.object.pk})


# --- ENVIRONMENT ---
class EnvironmentCreateView(LoginRequiredMixin, CreateView):
    model = Environment
    form_class = EnvironmentForm
    template_name = "form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("environment", kwargs={"environment_id": self.object.pk})


class EnvironmentUpdateView(LoginRequiredMixin, UpdateView):
    model = Environment
    form_class = EnvironmentForm
    template_name = "form.html"

    def get_queryset(self):
        return Environment.objects.filter(user=self.request.user)

    def get_success_url(self):
        return reverse("environment", kwargs={"environment_id": self.object.pk})


# --- MEASUREMENT ---
class MeasurementCreateView(LoginRequiredMixin, CreateView):
    model = Measurement
    form_class = MeasurementForm
    template_name = "form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("measurement", kwargs={"measurement_id": self.object.pk})


class MeasurementUpdateView(LoginRequiredMixin, UpdateView):
    model = Measurement
    form_class = MeasurementForm
    template_name = "form.html"

    def get_queryset(self):
        return Measurement.objects.filter(user=self.request.user)

    def get_success_url(self):
        return reverse("measurement", kwargs={"measurement_id": self.object.pk})


# --- UNIT ---
class UnitCreateView(LoginRequiredMixin, CreateView):
    model = Unit
    form_class = UnitForm
    template_name = "form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("unit", kwargs={"unit_id": self.object.pk})


class UnitUpdateView(LoginRequiredMixin, UpdateView):
    model = Unit
    form_class = UnitForm
    template_name = "form.html"

    def get_queryset(self):
        return Unit.objects.filter(user=self.request.user)

    def get_success_url(self):
        return reverse("unit", kwargs={"unit_id": self.object.pk})


# --- UNITTYPE ---
class UnittypeCreateView(LoginRequiredMixin, CreateView):
    model = Unittype
    form_class = UnittypeForm
    template_name = "form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("unittype", kwargs={"unittype_id": self.object.pk})


class UnittypeUpdateView(LoginRequiredMixin, UpdateView):
    model = Unittype
    form_class = UnittypeForm
    template_name = "form.html"

    def get_queryset(self):
        return Unittype.objects.filter(user=self.request.user)

    def get_success_url(self):
        return reverse("unittype", kwargs={"unittype_id": self.object.pk})


# --- ACTIONCATEGORY ---
class ActioncategoryCreateView(LoginRequiredMixin, CreateView):
    model = Actioncategory
    form_class = ActioncategoryForm
    template_name = "form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("actioncategory", kwargs={"actioncategory_id": self.object.pk})


class ActioncategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Actioncategory
    form_class = ActioncategoryForm
    template_name = "form.html"

    def get_queryset(self):
        return Actioncategory.objects.filter(user=self.request.user)

    def get_success_url(self):
        return reverse("actioncategory", kwargs={"actioncategory_id": self.object.pk})


# --- ACTIONTYPE ---
class ActiontypeCreateView(LoginRequiredMixin, CreateView):
    model = Actiontype
    form_class = ActiontypeForm
    template_name = "form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("actiontype", kwargs={"actiontype_id": self.object.pk})


class ActiontypeUpdateView(LoginRequiredMixin, UpdateView):
    model = Actiontype
    form_class = ActiontypeForm
    template_name = "form.html"

    def get_queryset(self):
        return Actiontype.objects.filter(user=self.request.user)

    def get_success_url(self):
        return reverse("actiontype", kwargs={"actiontype_id": self.object.pk})


# --- ACTIONLOG ---
class ActionLogCreateView(LoginRequiredMixin, CreateView):
    model = ActionLog
    form_class = ActionLogForm
    template_name = "form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("actionlog", kwargs={"actionlog_id": self.object.pk})


class ActionLogUpdateView(LoginRequiredMixin, UpdateView):
    model = ActionLog
    form_class = ActionLogForm
    template_name = "form.html"

    def get_queryset(self):
        return ActionLog.objects.filter(user=self.request.user)

    def get_success_url(self):
        return reverse("actionlog", kwargs={"actionlog_id": self.object.pk})


# --- NUTRIENT ---
class NutrientCreateView(LoginRequiredMixin, CreateView):
    model = Nutrient
    form_class = NutrientForm
    template_name = "form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("nutrient", kwargs={"nutrient_id": self.object.pk})


class NutrientUpdateView(LoginRequiredMixin, UpdateView):
    model = Nutrient
    form_class = NutrientForm
    template_name = "form.html"

    def get_queryset(self):
        return Nutrient.objects.filter(user=self.request.user)

    def get_success_url(self):
        return reverse("nutrient", kwargs={"nutrient_id": self.object.pk})


# --- NUTRITION ---
class NutritionCreateView(LoginRequiredMixin, CreateView):
    model = Nutrition
    form_class = NutritionForm
    template_name = "form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("nutrition", kwargs={"nutrition_id": self.object.pk})


class NutritionUpdateView(LoginRequiredMixin, UpdateView):
    model = Nutrition
    form_class = NutritionForm
    template_name = "form.html"

    def get_queryset(self):
        return Nutrition.objects.filter(user=self.request.user)

    def get_success_url(self):
        return reverse("nutrition", kwargs={"nutrition_id": self.object.pk})


# --- GROUP ---
class GroupCreateView(LoginRequiredMixin, CreateView):
    model = Group
    form_class = GroupForm
    template_name = "form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("group", kwargs={"group_id": self.object.pk})


class GroupUpdateView(LoginRequiredMixin, UpdateView):
    model = Group
    form_class = GroupForm
    template_name = "form.html"

    def get_queryset(self):
        return Group.objects.filter(user=self.request.user)

    def get_success_url(self):
        return reverse("group", kwargs={"group_id": self.object.pk})


# --- MEASUREMENTTYPE ---
class MeasurementtypeCreateView(LoginRequiredMixin, CreateView):
    model = Measurementtype
    form_class = MeasurementtypeForm
    template_name = "form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("measurementtype", kwargs={"measurementtype_id": self.object.pk})


class MeasurementtypeUpdateView(LoginRequiredMixin, UpdateView):
    model = Measurementtype
    form_class = MeasurementtypeForm
    template_name = "form.html"

    def get_queryset(self):
        return Measurementtype.objects.filter(user=self.request.user)

    def get_success_url(self):
        return reverse("measurementtype", kwargs={"measurementtype_id": self.object.pk})
