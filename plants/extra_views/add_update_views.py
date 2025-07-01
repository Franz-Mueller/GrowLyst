# plants/views_forms.py (example name)

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
    success_url = reverse_lazy("plants")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PlantUpdateView(LoginRequiredMixin, UpdateView):
    model = Plant
    form_class = PlantForm
    template_name = "form.html"
    success_url = reverse_lazy("plants")

    def get_queryset(self):
        return Plant.objects.filter(user=self.request.user)


# --- PLANTSTAGE ---
class PlantstageCreateView(LoginRequiredMixin, CreateView):
    model = Plantstage
    form_class = PlantstageForm
    template_name = "form.html"
    success_url = reverse_lazy("plantstages")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PlantstageUpdateView(LoginRequiredMixin, UpdateView):
    model = Plantstage
    form_class = PlantstageForm
    template_name = "form.html"
    success_url = reverse_lazy("plantstages")

    def get_queryset(self):
        return Plantstage.objects.filter(user=self.request.user)


# --- PLANTSTAGELOG ---
class PlantstagelogCreateView(LoginRequiredMixin, CreateView):
    model = Plantstagelog
    form_class = PlantstagelogForm
    template_name = "form.html"
    success_url = reverse_lazy("plantstagelogs")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PlantstagelogUpdateView(LoginRequiredMixin, UpdateView):
    model = Plantstagelog
    form_class = PlantstagelogForm
    template_name = "form.html"
    success_url = reverse_lazy("plantstagelogs")

    def get_queryset(self):
        return Plantstagelog.objects.filter(user=self.request.user)


# --- STRAIN ---
class StrainCreateView(LoginRequiredMixin, CreateView):
    model = Strain
    form_class = StrainForm
    template_name = "form.html"
    success_url = reverse_lazy("strains")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class StrainUpdateView(LoginRequiredMixin, UpdateView):
    model = Strain
    form_class = StrainForm
    template_name = "form.html"
    success_url = reverse_lazy("strains")

    def get_queryset(self):
        return Strain.objects.filter(user=self.request.user)


# --- BREEDER ---
class BreederCreateView(LoginRequiredMixin, CreateView):
    model = Breeder
    form_class = BreederForm
    template_name = "form.html"
    success_url = reverse_lazy("breeders")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class BreederUpdateView(LoginRequiredMixin, UpdateView):
    model = Breeder
    form_class = BreederForm
    template_name = "form.html"
    success_url = reverse_lazy("breeders")

    def get_queryset(self):
        return Breeder.objects.filter(user=self.request.user)


# --- MEDIUMTYPE ---
class MediumtypeCreateView(LoginRequiredMixin, CreateView):
    model = Mediumtype
    form_class = MediumtypeForm
    template_name = "form.html"
    success_url = reverse_lazy("mediumtypes")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class MediumtypeUpdateView(LoginRequiredMixin, UpdateView):
    model = Mediumtype
    form_class = MediumtypeForm
    template_name = "form.html"
    success_url = reverse_lazy("mediumtypes")

    def get_queryset(self):
        return Mediumtype.objects.filter(user=self.request.user)


# --- MEDIUM ---
class MediumCreateView(LoginRequiredMixin, CreateView):
    model = Medium
    form_class = MediumForm
    template_name = "form.html"
    success_url = reverse_lazy("mediums")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class MediumUpdateView(LoginRequiredMixin, UpdateView):
    model = Medium
    form_class = MediumForm
    template_name = "form.html"
    success_url = reverse_lazy("mediums")

    def get_queryset(self):
        return Medium.objects.filter(user=self.request.user)


# --- PLANTPHOTO ---
class PlantphotoCreateView(LoginRequiredMixin, CreateView):
    model = Plantphoto
    form_class = PlantphotoForm
    template_name = "form.html"
    success_url = reverse_lazy("plantphotos")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PlantphotoUpdateView(LoginRequiredMixin, UpdateView):
    model = Plantphoto
    form_class = PlantphotoForm
    template_name = "form.html"
    success_url = reverse_lazy("plantphotos")

    def get_queryset(self):
        return Plantphoto.objects.filter(user=self.request.user)


# --- GROW ---
class GrowCreateView(LoginRequiredMixin, CreateView):
    model = Grow
    form_class = GrowForm
    template_name = "form.html"
    success_url = reverse_lazy("grows")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class GrowUpdateView(LoginRequiredMixin, UpdateView):
    model = Grow
    form_class = GrowForm
    template_name = "form.html"
    success_url = reverse_lazy("grows")

    def get_queryset(self):
        return Grow.objects.filter(user=self.request.user)


# --- GROWTYPE ---
class GrowtypeCreateView(LoginRequiredMixin, CreateView):
    model = Growtype
    form_class = GrowtypeForm
    template_name = "form.html"
    success_url = reverse_lazy("growtypes")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class GrowtypeUpdateView(LoginRequiredMixin, UpdateView):
    model = Growtype
    form_class = GrowtypeForm
    template_name = "form.html"
    success_url = reverse_lazy("growtypes")

    def get_queryset(self):
        return Growtype.objects.filter(user=self.request.user)


# --- ENVIRONMENT ---
class EnvironmentCreateView(LoginRequiredMixin, CreateView):
    model = Environment
    form_class = EnvironmentForm
    template_name = "form.html"
    success_url = reverse_lazy("environments")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EnvironmentUpdateView(LoginRequiredMixin, UpdateView):
    model = Environment
    form_class = EnvironmentForm
    template_name = "form.html"
    success_url = reverse_lazy("environments")

    def get_queryset(self):
        return Environment.objects.filter(user=self.request.user)


# --- MEASUREMENT ---
class MeasurementCreateView(LoginRequiredMixin, CreateView):
    model = Measurement
    form_class = MeasurementForm
    template_name = "form.html"
    success_url = reverse_lazy("measurements")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class MeasurementUpdateView(LoginRequiredMixin, UpdateView):
    model = Measurement
    form_class = MeasurementForm
    template_name = "form.html"
    success_url = reverse_lazy("measurements")

    def get_queryset(self):
        return Measurement.objects.filter(user=self.request.user)


# --- UNIT ---
class UnitCreateView(LoginRequiredMixin, CreateView):
    model = Unit
    form_class = UnitForm
    template_name = "form.html"
    success_url = reverse_lazy("units")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UnitUpdateView(LoginRequiredMixin, UpdateView):
    model = Unit
    form_class = UnitForm
    template_name = "form.html"
    success_url = reverse_lazy("units")

    def get_queryset(self):
        return Unit.objects.filter(user=self.request.user)


# --- UNITTYPE ---
class UnittypeCreateView(LoginRequiredMixin, CreateView):
    model = Unittype
    form_class = UnittypeForm
    template_name = "form.html"
    success_url = reverse_lazy("unittypes")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UnittypeUpdateView(LoginRequiredMixin, UpdateView):
    model = Unittype
    form_class = UnittypeForm
    template_name = "form.html"
    success_url = reverse_lazy("unittypes")

    def get_queryset(self):
        return Unittype.objects.filter(user=self.request.user)


# --- ACTIONCATEGORY ---
class ActioncategoryCreateView(LoginRequiredMixin, CreateView):
    model = Actioncategory
    form_class = ActioncategoryForm
    template_name = "form.html"
    success_url = reverse_lazy("actioncategories")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ActioncategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Actioncategory
    form_class = ActioncategoryForm
    template_name = "form.html"
    success_url = reverse_lazy("actioncategories")

    def get_queryset(self):
        return Actioncategory.objects.filter(user=self.request.user)


# --- ACTIONTYPE ---
class ActiontypeCreateView(LoginRequiredMixin, CreateView):
    model = Actiontype
    form_class = ActiontypeForm
    template_name = "form.html"
    success_url = reverse_lazy("actiontypes")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ActiontypeUpdateView(LoginRequiredMixin, UpdateView):
    model = Actiontype
    form_class = ActiontypeForm
    template_name = "form.html"
    success_url = reverse_lazy("actiontypes")

    def get_queryset(self):
        return Actiontype.objects.filter(user=self.request.user)


# --- ACTIONLOG ---
class ActionLogCreateView(LoginRequiredMixin, CreateView):
    model = ActionLog
    form_class = ActionLogForm
    template_name = "form.html"
    success_url = reverse_lazy("actionlogs")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ActionLogUpdateView(LoginRequiredMixin, UpdateView):
    model = ActionLog
    form_class = ActionLogForm
    template_name = "form.html"
    success_url = reverse_lazy("actionlogs")

    def get_queryset(self):
        return ActionLog.objects.filter(user=self.request.user)


# --- NUTRIENT ---
class NutrientCreateView(LoginRequiredMixin, CreateView):
    model = Nutrient
    form_class = NutrientForm
    template_name = "form.html"
    success_url = reverse_lazy("nutrients")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class NutrientUpdateView(LoginRequiredMixin, UpdateView):
    model = Nutrient
    form_class = NutrientForm
    template_name = "form.html"
    success_url = reverse_lazy("nutrients")

    def get_queryset(self):
        return Nutrient.objects.filter(user=self.request.user)


# --- NUTRITION ---
class NutritionCreateView(LoginRequiredMixin, CreateView):
    model = Nutrition
    form_class = NutritionForm
    template_name = "form.html"
    success_url = reverse_lazy("nutritions")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class NutritionUpdateView(LoginRequiredMixin, UpdateView):
    model = Nutrition
    form_class = NutritionForm
    template_name = "form.html"
    success_url = reverse_lazy("nutritions")

    def get_queryset(self):
        return Nutrition.objects.filter(user=self.request.user)


# --- GROUP ---
class GroupCreateView(LoginRequiredMixin, CreateView):
    model = Group
    form_class = GroupForm
    template_name = "form.html"
    success_url = reverse_lazy("groups")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class GroupUpdateView(LoginRequiredMixin, UpdateView):
    model = Group
    form_class = GroupForm
    template_name = "form.html"
    success_url = reverse_lazy("groups")

    def get_queryset(self):
        return Group.objects.filter(user=self.request.user)


# --- MEASUREMENTTYPE ---
class MeasurementtypeCreateView(LoginRequiredMixin, CreateView):
    model = Measurementtype
    form_class = MeasurementtypeForm
    template_name = "form.html"
    success_url = reverse_lazy("measurementtypes")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class MeasurementtypeUpdateView(LoginRequiredMixin, UpdateView):
    model = Measurementtype
    form_class = MeasurementtypeForm
    template_name = "form.html"
    success_url = reverse_lazy("measurementtypes")

    def get_queryset(self):
        return Measurementtype.objects.filter(user=self.request.user)
