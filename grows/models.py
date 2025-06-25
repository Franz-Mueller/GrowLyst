from django.db import models


class Grow(models.Model):
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="grows",
        blank=True,
        null=True,
    )
    type = models.CharField(
        max_length=50,
        choices=[
            ("flower", "Flower"),
            ("mothers", "Mothers"),
            ("breeding", "Breeding"),
            ("other", "Other"),
        ],
        default="flower",
    )
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(
        upload_to="grows/", blank=True, null=True
    )  # TODO Implement image upload
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Grow for {self.user.username if self.user else 'Unknown User'}"


class Environment(models.Model):
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="grows",
        blank=True,
        null=True,
    )
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        upload_to="environments/", blank=True, null=True
    )  # TODO Implement image upload

    def __str__(self):
        return f"Environment for {self.grow.user.username if self.grow else 'Unknown User'}"


class Measurement(models.Model):
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="measurements",
        blank=True,
        null=True,
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
    value = models.FloatField(blank=True, null=True)
    unit = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Measurement {self.name} for {self.grow.name if self.grow else 'Unknown Grow'}"


class Unit(models.Model):
    name = models.CharField(max_length=50, unique=True)
    symbol = models.CharField(max_length=10, unique=True)
    conversion_factor_to_base = models.FloatField(default=1.0)

    def __str__(self):
        return f"{self.name} ({self.symbol})"


class Unittype(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    icon = models.ImageField(
        upload_to="unit_types/", blank=True, null=True
    )  # TODO Implement image upload
    baseunit = models.ForeignKey(
        "Unit",
        on_delete=models.CASCADE,
        related_name="baseunit",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name


class Actioncategory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    icon = models.ImageField(
        upload_to="action_categories/", blank=True, null=True
    )  # TODO Implement image upload

    def __str__(self):
        return self.name


class Actiontype(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    icon = models.ImageField(
        upload_to="action_types/", blank=True, null=True
    )  # TODO Implement image upload
    category = models.ForeignKey(
        Actioncategory,
        on_delete=models.CASCADE,
        related_name="action_types",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name


class ActionLog(models.Model):
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="actions",
        blank=True,
        null=True,
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
    before_image = models.ImageField(
        upload_to="actions/before/", blank=True, null=True
    )  # TODO Implement image upload
    after_image = models.ImageField(
        upload_to="actions/after/", blank=True, null=True
    )  # TODO Implement image upload
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Action {self.action_type.name} for {self.grow.name if self.grow else 'Unknown Grow'}"


class Nutrient(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(
        upload_to="nutrients/", blank=True, null=True
    )  # TODO Implement image upload
    producer = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Nutrition(models.Model):
    user = models.ForeignKey(
        "users.User",
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


class Group(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(
        upload_to="groups/", blank=True, null=True
    )  # TODO implement Image
    grow = models.ForeignKey(
        "Grow",
        on_delete=models.CASCADE,
        related_name="groups",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name
