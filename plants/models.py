from django.db import models


# region Plant
class PlantQuerySet(models.QuerySet):
    def recent(self):
        return self.order_by("-updated_at")

    def for_user(self, user):
        return self.filter(user=user)


class PlantManager(models.Manager):
    def get_queryset(self):
        return PlantQuerySet(self.model, using=self._db)

    def for_user(self, user):
        return self.get_queryset().for_user(user)

    def recent_for_user(self, user, limit=3):
        return self.get_queryset().for_user(user).recent()[:limit]


class Plant(models.Model):
    objects = PlantManager()
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
    profile_image = models.ImageField(
        upload_to="plant_profiles/", blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# endregion Plant


# region Plantstage
class PlantstageQuerySet(models.QuerySet): ...


class PlantstageManager(models.Manager):
    def get_queryset(self):
        return PlantstageQuerySet(self.model, using=self._db)


class Plantstage(models.Model):
    objects = PlantstageManager()
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# endregion Plantstage


# region PlantstageLog
class PlantstagelogQuerySet(models.QuerySet): ...


class PlantstagelogManager(models.Manager):
    def get_queryset(self):
        return PlantstagelogQuerySet(self.model, using=self._db)


class Plantstagelog(models.Model):
    objects = PlantstagelogManager()
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


# endregion PlantstageLog


# region Strain
class StrainQuerySet(models.QuerySet): ...


class StrainManager(models.Manager):
    def get_queryset(self):
        return StrainQuerySet(self.model, using=self._db)


class Strain(models.Model):
    objects = StrainManager()
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
    def __str__(self):
        return self.name


# endregion Strain


# region Breeder
class BreederQuerySet(models.QuerySet): ...


class BreederManager(models.Manager):
    def get_queryset(self):
        return BreederQuerySet(self.model, using=self._db)


class Breeder(models.Model):
    objects = BreederManager()
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


# endregion Breeder


# region Mediumtype
class MediumtypeQuerySet(models.QuerySet): ...


class MediumtypeManager(models.Manager):
    def get_queryset(self):
        return MediumtypeQuerySet(self.model, using=self._db)


class Mediumtype(models.Model):
    objects = MediumtypeManager()
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


# endregion Mediumtype


# region Medium
class MediumQuerySet(models.QuerySet): ...


class MediumManager(models.Manager):
    def get_queryset(self):
        return MediumQuerySet(self.model, using=self._db)


class Medium(models.Model):
    objects = MediumManager()
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


# endregion Medium


# region Plantphoto
class PlantphotoQuerySet(models.QuerySet): ...


class PlantphotoManager(models.Manager):
    def get_queryset(self):
        return PlantphotoQuerySet(self.model, using=self._db)


class Plantphoto(models.Model):
    objects = PlantphotoManager()
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


# endregion Plantphoto
