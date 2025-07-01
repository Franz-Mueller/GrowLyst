# plants/forms.py

from django import forms
from ..models import *


class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        exclude = ["user", "created_at", "updated_at"]


class PlantstageForm(forms.ModelForm):
    class Meta:
        model = Plantstage
        exclude = ["user", "created_at", "updated_at"]


class PlantstagelogForm(forms.ModelForm):
    class Meta:
        model = Plantstagelog
        exclude = ["user", "created_at", "updated_at"]


class StrainForm(forms.ModelForm):
    class Meta:
        model = Strain
        exclude = ["user", "created_at", "updated_at"]


class BreederForm(forms.ModelForm):
    class Meta:
        model = Breeder
        exclude = ["user", "created_at", "updated_at"]


class MediumtypeForm(forms.ModelForm):
    class Meta:
        model = Mediumtype
        exclude = ["user", "created_at", "updated_at"]


class MediumForm(forms.ModelForm):
    class Meta:
        model = Medium
        exclude = ["user", "created_at", "updated_at"]


class PlantphotoForm(forms.ModelForm):
    class Meta:
        model = Plantphoto
        exclude = ["user", "created_at", "updated_at"]


class GrowForm(forms.ModelForm):
    class Meta:
        model = Grow
        exclude = ["user", "created_at", "updated_at"]


class GrowtypeForm(forms.ModelForm):
    class Meta:
        model = Growtype
        exclude = ["user", "created_at", "updated_at"]


class EnvironmentForm(forms.ModelForm):
    class Meta:
        model = Environment
        exclude = ["user", "created_at", "updated_at"]


class MeasurementForm(forms.ModelForm):
    class Meta:
        model = Measurement
        exclude = ["user", "created_at", "updated_at"]


class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        exclude = ["user", "created_at", "updated_at"]


class UnittypeForm(forms.ModelForm):
    class Meta:
        model = Unittype
        exclude = ["user", "created_at", "updated_at"]


class ActioncategoryForm(forms.ModelForm):
    class Meta:
        model = Actioncategory
        exclude = ["user", "created_at", "updated_at"]


class ActiontypeForm(forms.ModelForm):
    class Meta:
        model = Actiontype
        exclude = ["user", "created_at", "updated_at"]


class ActionLogForm(forms.ModelForm):
    class Meta:
        model = ActionLog
        exclude = ["user", "created_at", "updated_at"]


class NutrientForm(forms.ModelForm):
    class Meta:
        model = Nutrient
        exclude = ["user", "created_at", "updated_at"]


class NutritionForm(forms.ModelForm):
    class Meta:
        model = Nutrition
        exclude = ["user", "created_at", "updated_at"]


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        exclude = ["user", "created_at", "updated_at"]


class MeasurementtypeForm(forms.ModelForm):
    class Meta:
        model = Measurementtype
        exclude = ["user", "created_at", "updated_at"]
