from django.db import models


class Plant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    strain = models.ForeignKey(  # TODO autogenerate plant name by strain name + pheno #x / clone #x
        "Strain",
        on_delete=models.SET_NULL,
        related_name="plants",
        blank=True,
        null=True,
    )
    environment = models.ForeignKey(  # Required
        "grows.Environment",
        on_delete=models.CASCADE,  # TODO user should be warned that he will delete plants inside the env as well
        related_name="plants",
        blank=False,
        null=False,
    )
    grow = models.ForeignKey(  # Not required TODO warn user before deletion
        "grows.Grow",
        on_delete=models.SET_NULL,
        related_name="plants",
        blank=True,
        null=True,
    )
    group = models.ForeignKey(  # Not required TODO warn user before deletion
        "grows.Group",
        on_delete=models.SET_NULL,
        related_name="plants",
        blank=True,
        null=True,
    )
    user = models.ForeignKey(  # required
        "auth.User",
        on_delete=models.CASCADE,
        related_name="plants",
    )
    medium = models.ForeignKey(
        "Medium",
        on_delete=models.SET_NULL,
        related_name="plants",
        blank=True,
        null=True,
    )
    type = models.ForeignKey(
        "Planttype",
        on_delete=models.SET_NULL,
        related_name="plants",
        blank=True,
        null=True,
    )
    # image = models.ImageField( upload_to="plants/", blank=True, null=True)  # TODO implement Image
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):  # TODO implement __str__ method
        return self.name


class Planttype(models.Model):
    user = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
        related_name="planttypes",
        blank=True,
        null=True,
    )
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Plantstage(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Plantstagelog(models.Model):
    user = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
        related_name="plant_stage_logs",
    )
    plant = models.ForeignKey(
        "Plant",
        on_delete=models.CASCADE,
        related_name="plant_stage_logs",
    )
    plantstage = models.ForeignKey(
        "Plantstage", on_delete=models.CASCADE, related_name="plant_stage_logs"
    )
    date_of_change = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Strain(models.Model):
    user = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
        related_name="strains",
        blank=True,
        null=True,
    )
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    breeder = models.ForeignKey(
        "Breeder",
        on_delete=models.PROTECT,
        related_name="strains",
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # image = models.ImageField(pload_to="strains/", blank=True, null=True)  # TODO implement Image


class Breeder(models.Model):
    user = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
        related_name="breeders",
        blank=True,
        null=True,
    )
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    # image = models.ImageField(upload_to="breeders/", blank=True, null=True)  # TODO implement Image
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Mediumtype(models.Model):
    user = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
        related_name="mediumtypes",
        blank=True,
        null=True,
    )
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Medium(models.Model):
    user = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
        related_name="mediums",
        blank=True,
        null=True,
    )
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    medium_type = models.ForeignKey(
        "Mediumtype",
        on_delete=models.CASCADE,
        related_name="mediums",
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Plantphoto(models.Model):
    user = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
        related_name="plant_photos",
    )
    plant = models.ForeignKey(
        "Plant",
        on_delete=models.CASCADE,
        related_name="photos",
        blank=True,
        null=True,
    )
    # image = models.ImageField(upload_to="plant_photos/", blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Photo for {self.plant.name if self.plant else 'Unknown Plant'}"
