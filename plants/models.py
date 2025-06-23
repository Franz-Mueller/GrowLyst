from django.db import models


class Plant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    strain = models.OneToOneField(
        "Strain", on_delete=models.CASCADE, related_name="plant", blank=True, null=True
    )
    environment = models.OneToOneField(
        "Environment",
        on_delete=models.CASCADE,
        related_name="plant",
        blank=True,
        null=True,
    )
    grow = models.OneToOneField(
        "Grow", on_delete=models.CASCADE, related_name="plant", blank=True, null=True
    )
    user = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
        related_name="plants",
        blank=True,
        null=True,
    )
    current_stage = models.ForeignKey(
        "Stage",
        on_delete=models.CASCADE,
        related_name="current_plants",
        blank=True,
        null=True,
    )
    mediumtype = models.ForeignKey(
        "Mediumtype",
        on_delete=models.CASCADE,
        related_name="plants",
        blank=True,
        null=True,
    )
    medium = models.ForeignKey(
        "Medium",
        on_delete=models.CASCADE,
        related_name="plants",
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to="plants/", blank=True, null=True
    )  # TODO implement Image
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    image = models.ImageField(upload_to="plants/", blank=True, null=True)

    def __str__(self):
        return self.name


class Plantstage(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)


class Plantstagechange(models.Model):
    user = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
        related_name="plant_stage_changes",
        blank=True,
        null=True,
    )
    plant = models.ForeignKey(
        "Plant",
        on_delete=models.CASCADE,
        related_name="stage_changes",
        blank=True,
        null=True,
    )
    plantstage = models.ForeignKey(
        "Plantstage", on_delete=models.CASCADE, related_name="changes"
    )
    date = models.DateTimeField(auto_now_add=True)


class Strain(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    breeder = models.ForeignKey(
        "Breeder",
        on_delete=models.CASCADE,
        related_name="strains",
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to="strains/", blank=True, null=True
    )  # TODO implement Image


class Mediumtype(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Medium(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    medium_type = models.ForeignKey(
        "Mediumtype",
        on_delete=models.CASCADE,
        related_name="mediums",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name


class Breeder(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    image = models.ImageField(
        upload_to="breeders/", blank=True, null=True
    )  # TODO implement Image

    def __str__(self):
        return self.name


class Plantphoto(models.Model):
    user = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
        related_name="plant_photos",
        blank=True,
        null=True,
    )
    plant = models.ForeignKey(
        "Plant",
        on_delete=models.CASCADE,
        related_name="photos",
        blank=True,
        null=True,
    )
    image = models.ImageField(upload_to="plant_photos/", blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Photo for {self.plant.name if self.plant else 'Unknown Plant'}"
