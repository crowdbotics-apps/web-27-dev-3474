from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    name = models.CharField(null=True, blank=True, max_length=255,)
    test = models.ForeignKey(
        "home.CustomText",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="user_test",
    )
    testt = models.ForeignKey(
        "home.CustomText",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="user_testt",
    )
    testtt = models.ForeignKey(
        "home.CustomText",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="user_testtt",
    )
    tghrtg = models.ForeignKey(
        "users.User",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="user_tghrtg",
    )
    sfdarsdf = models.ForeignKey(
        "home.CustomText",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="user_sfdarsdf",
    )

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
