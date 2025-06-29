from django.db import models


# region Grow
class Grow(models.Model):
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
class Growtype(models.Model):
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
class Environment(models.Model):
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
class Measurement(models.Model):
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
        "plants.Plant",
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
class Unit(models.Model):
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
class Unittype(models.Model):
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
class Actioncategory(models.Model):
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


class Actiontype(models.Model):
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


class ActionLog(models.Model):
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
        "plants.Plant",
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
class Nutrient(models.Model):
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
class Nutrition(models.Model):
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
class Group(models.Model):  # TODO maybe rework so it is not assigned to grow and user
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
class Measurementtype(models.Model):
    user = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, blank=True, null=True
    )
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    unittype = models.ForeignKey("Unittype", on_delete=models.PROTECT)

    def __str__(self):
        return self.name


# endregion Measurementtype
