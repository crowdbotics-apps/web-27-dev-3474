from django.conf import settings
from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    title = models.CharField(max_length=150,)
    ttestt = models.ForeignKey(
        "home.CustomText",
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name="customtext_ttestt",
    )
    ttesttt = models.ForeignKey(
        "home.CustomText",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="customtext_ttesttt",
    )
    test = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="customtext_test",
    )

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"


class HomePage(models.Model):
    body = models.TextField()
    czvfc = models.ForeignKey(
        "home.CustomText",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="homepage_czvfc",
    )
    ghcgv = models.ForeignKey(
        "home.HomePage",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="homepage_ghcgv",
    )

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"
