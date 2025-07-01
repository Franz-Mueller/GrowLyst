from django import forms
from .models import Plant


class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        # You can specify fields = '__all__' or list only those you want
        fields = [
            "name",
            "description",
            "strain",
            "environment",
            "grow",
            "group",
            "medium",
            "profile_image",
        ]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 3}),
            # You can add more widgets to customize the form
        }
