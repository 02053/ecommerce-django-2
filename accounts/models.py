from django.db import models
from django.contrib.auth.models import AbstractUser


class Buyer(AbstractUser):
    country = models.CharField(null=True, blank=True, max_length=30)
    city = models.CharField(null=True, blank=True, max_length=30)
    region = models.CharField(null=True, blank=True, max_length=30)
    address = models.CharField(null=True, blank=True, max_length=30)
    postal_code = models.CharField(null=True, blank=True, max_length=30)
    number_phone = models.CharField(null=True, blank=True, max_length=30)

    class Meta:
        verbose_name_plural = 'Buyer'

    def __str__(self) -> str:
        return self.username
