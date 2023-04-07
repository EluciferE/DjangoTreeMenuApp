from django.db import models
from django.core.exceptions import ValidationError


class Menu(models.Model):
    name = models.CharField(verbose_name="Name", max_length=100, help_text="maximum 100 characters")
    slug = models.SlugField(verbose_name="Slug")

    @property
    def children(self):
        return MenuBranch.objects.filter(menu=self, parent__isnull=True)

    class Meta:
        verbose_name_plural = "Menus"
        verbose_name = "Menu"

    def __str__(self):
        return f"{self.name} (/{self.slug})"


class MenuBranch(models.Model):
    menu = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE,
        verbose_name="Menu",
    )

    name = models.CharField(
        verbose_name="Branch name",
        max_length=100,
        help_text="maximum 100 characters",
    )

    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        verbose_name="Parent branch",
        help_text="Leave the field blank if attached to the menu",
        related_name='children',
        null=True,
        blank=True,
    )

    def clean(self):
        """
        Check parent to avoid circular relationship
        """
        if self.parent is None:
            return

        if self.parent == self:
            raise ValidationError("Cannot set self as parent branch")
        if self.parent.parent == self:
            raise ValidationError("Cannot set child as self parent")
        if self.parent.menu != self.menu:
            raise ValidationError("Cannot set parent from another menu")

    class Meta:
        verbose_name_plural = "Branches"
        verbose_name = "Branch"

    def __str__(self):
        return f"{self.menu.name} - {self.name}"
