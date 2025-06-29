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
        "Environment",
        on_delete=models.CASCADE,  # TODO user should be warned that he will delete plants inside the env as well
        related_name="plants",
        blank=False,
        null=False,
    )
    grow = models.ForeignKey(  # Not required TODO warn user before deletion
        "Grow",
        on_delete=models.SET_NULL,
        related_name="plants",
        blank=True,
        null=True,
    )
    group = models.ForeignKey(  # Not required TODO warn user before deletion
        "Group",
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
"""
TODO: Implement Custom User Plantstage and view
For now we do not need custom user plant stages.
For now we use the admin panel.
"""


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
"""
TODO: Design and implement plant stage log logic
"""


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
"""
TODO: Implement custom user strain and view.
For now the user does not need to create custom strains.
"""


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
    image = models.ImageField(upload_to="plant_photos/", blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Photo for {self.plant.name if self.plant else 'Unknown Plant'}"


# endregion Plantphoto
from django.db import models


# region Grow
class GrowQuerySet(models.QuerySet): ...


class GrowManager(models.Manager):
    def get_queryset(self):
        return GrowQuerySet(self.model, using=self._db)


class Grow(models.Model):
    objects = GrowManager()
    user = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
        related_name="grows",
    )
    type = models.ForeignKey(
        "Growtype", on_delete=models.SET_NULL, blank=True, null=True
    )
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    # image = models.ImageField(upload_to="grows/", blank=True, null=True)  # TODO Implement image upload
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# endregion Grow
# region Growtype
class GrowtypeQuerySet(models.QuerySet): ...


class GrowtypeManager(models.Manager):
    def get_queryset(self):
        return GrowtypeQuerySet(self.model, using=self._db)


class Growtype(models.Model):
    objects = GrowtypeManager()
    user = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
        related_name="growtypes",
        blank=True,
        null=True,
    )
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# endregion Growtype
# region Environment
class EnvironmentQuerySet(models.QuerySet): ...


class EnvironmentManager(models.Manager):
    def get_queryset(self):
        return EnvironmentQuerySet(self.model, using=self._db)


class Environment(models.Model):
    objects = EnvironmentManager()
    user = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
        related_name="environments",
        blank=True,
        null=True,
    )
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # image = models.ImageField(upload_to="environments/", blank=True, null=True)  # TODO Implement image upload

    def __str__(self):
        return self.name


# endregion Environment


# region Measurement
class MeasurementQuerySet(models.QuerySet): ...


class MeasurementManager(models.Manager):
    def get_queryset(self):
        return MeasurementQuerySet(self.model, using=self._db)


class Measurement(models.Model):
    objects = MeasurementManager()
    user = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
        related_name="measurements",
    )
    grow = models.ForeignKey(
        Grow,
        on_delete=models.CASCADE,
        related_name="measurements",
        blank=True,
        null=True,
    )
    environment = models.ForeignKey(
        Environment,
        on_delete=models.CASCADE,
        related_name="measurements",
        blank=True,
        null=True,
    )
    plant = models.ForeignKey(
        "Plant",
        on_delete=models.CASCADE,
        related_name="measurements",
        blank=True,
        null=True,
    )
    unit = models.ForeignKey(
        "Unit",
        on_delete=models.CASCADE,
        related_name="measurements",
        blank=True,
        null=True,
    )
    measurementtype = models.ForeignKey(
        "Measurementtype",
        on_delete=models.CASCADE,
        related_name="measurements",
        null=True,
        blank=True,
    )
    value = models.FloatField()
    unit = models.ForeignKey(
        "Unit",
        on_delete=models.PROTECT,
        related_name="measurement",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Measurement for {self.grow.name if self.grow else 'Unknown Grow'}"


# endregion Measurement


# region Unit
class UnitQuerySet(models.QuerySet): ...


class UnitManager(models.Manager):
    def get_queryset(self):
        return UnitQuerySet(self.model, using=self._db)


class Unit(models.Model):
    objects = UnitManager()
    user = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
        related_name="units",
        blank=True,
        null=True,
    )
    name = models.CharField(max_length=50, unique=True)
    symbol = models.CharField(max_length=10, unique=True)
    conversion_factor_to_base = models.FloatField(default=1.0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# endregion Unit


# region Unittype
class UnittypeQuerySet(models.QuerySet): ...


class UnittypeManager(models.Manager):
    def get_queryset(self):
        return UnittypeQuerySet(self.model, using=self._db)


class Unittype(models.Model):
    objects = UnittypeManager()
    user = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
        related_name="unittypes",
        blank=True,
        null=True,
    )
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    # icon = models.ImageField(upload_to="unit_types/", blank=True, null=True)  # TODO Implement image upload
    baseunit = models.ForeignKey(
        "Unit",
        on_delete=models.CASCADE,
        related_name="Unittypes",
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# endregion Unittype
# region Actioncategory
class ActioncategoryQuerySet(models.QuerySet): ...


class ActioncategoryManager(models.Manager):
    def get_queryset(self):
        return ActioncategoryQuerySet(self.model, using=self._db)


class Actioncategory(models.Model):
    objects = ActioncategoryManager()
    user = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
        related_name="Actioncategories",
        blank=True,
        null=True,
    )
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    # icon = models.ImageField(upload_to="action_categories/", blank=True, null=True)  # TODO Implement image upload
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# region Actioncategory


# region Actiontype
class ActiontypeQuerySet(models.QuerySet): ...


class ActiontypeManager(models.Manager):
    def get_queryset(self):
        return ActiontypeQuerySet(self.model, using=self._db)


class Actiontype(models.Model):
    objects = ActiontypeManager()
    user = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
        related_name="actiontypes",
        blank=True,
        null=True,
    )
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    # icon = models.ImageField(upload_to="action_types/", blank=True, null=True)  # TODO Implement image upload
    category = models.ForeignKey(
        Actioncategory,
        on_delete=models.CASCADE,
        related_name="action_types",
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# endregion Actiontype


# region ActionLog
class ActionLogQuerySet(models.QuerySet): ...


class ActionLogManager(models.Manager):
    def get_queryset(self):
        return ActionLogQuerySet(self.model, using=self._db)


class ActionLog(models.Model):
    objects = ActionLogManager()
    user = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
        related_name="actions",
    )
    grow = models.ForeignKey(
        Grow,
        on_delete=models.CASCADE,
        related_name="actions",
        blank=True,
        null=True,
    )
    environment = models.ForeignKey(
        Environment,
        on_delete=models.CASCADE,
        related_name="actions",
        blank=True,
        null=True,
    )
    plant = models.ForeignKey(
        "Plant",
        on_delete=models.CASCADE,
        related_name="actions",
        blank=True,
        null=True,
    )
    Actioncategory = models.ForeignKey(
        Actioncategory,
        on_delete=models.CASCADE,
        related_name="actions",
        blank=True,
        null=True,
    )
    action_type = models.ForeignKey(
        Actiontype,
        on_delete=models.CASCADE,
        related_name="actions",
        blank=True,
        null=True,
    )
    description = models.TextField(blank=True, null=True)
    # before_image = models.ImageField(upload_to="actions/before/", blank=True, null=True)  # TODO Implement image upload
    # after_image = models.ImageField(upload_to="actions/after/", blank=True, null=True)  # TODO Implement image upload
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# endregion ActionLog


# region Nutrient
class NutrientQuerySet(models.QuerySet): ...


class NutrientManager(models.Manager):
    def get_queryset(self):
        return NutrientQuerySet(self.model, using=self._db)


class Nutrient(models.Model):
    objects = NutrientManager()
    user = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
        related_name="nutrients",
        blank=True,
        null=True,
    )
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    # image = models.ImageField(upload_to="nutrients/", blank=True, null=True)  # TODO Implement image upload
    producer = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# endregion Nutrient


# region Nutrition
class NutritionQuerySet(models.QuerySet): ...


class NutritionManager(models.Manager):
    def get_queryset(self):
        return NutritionQuerySet(self.model, using=self._db)


class Nutrition(models.Model):
    objects = NutritionManager()
    user = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
        related_name="nutritions",
        blank=True,
        null=True,
    )
    actionlog = models.ForeignKey(
        ActionLog,
        on_delete=models.CASCADE,
        related_name="nutritions",
        blank=True,
        null=True,
    )
    nutrient = models.ForeignKey(
        Nutrient,
        on_delete=models.CASCADE,
        related_name="nutritions",
        blank=True,
        null=True,
    )
    amount = models.FloatField(blank=True, null=True)
    unit = models.ForeignKey(
        Unit,
        on_delete=models.CASCADE,
        related_name="nutritions",
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# endregion Nutrition


# region Group
class GroupQuerySet(models.QuerySet): ...


class GroupManager(models.Manager):
    def get_queryset(self):
        return GroupQuerySet(self.model, using=self._db)


class Group(models.Model):  # TODO maybe rework so it is not assigned to grow and user
    objects = GroupManager()
    user = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
        related_name="plantgroups",
        blank=True,
        null=True,
    )
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# endregion Group
# region Measurementtype
class MeasurementtypeQuerySet(models.QuerySet): ...


class MeasurementtypeManager(models.Manager):
    def get_queryset(self):
        return MeasurementtypeQuerySet(self.model, using=self._db)


class Measurementtype(models.Model):
    objects = MeasurementtypeManager()
    user = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, blank=True, null=True
    )
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    unittype = models.ForeignKey("Unittype", on_delete=models.PROTECT)

    def __str__(self):
        return self.name


# endregion Measurementtype
