from django.core.validators import MinLengthValidator
from django.db import models

from accounts.models import AccountUser


class Seller(models.Model):
    name = models.CharField(
        max_length=40,
    )
    description = models.TextField()
    city = models.CharField(
        max_length=40,
    )
    address = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )
    photo = models.ImageField(
        upload_to='sellers/',
        null=True,
        blank=True,
    )
    website_url = models.URLField(
        null=True,
        blank=True,
    )
    contact_email = models.EmailField()
    contact_phone = models.CharField(
        max_length=16,
        validators=(
            MinLengthValidator(8),
        ),
        null=True,
        blank=True,
    )
    approved = models.BooleanField()
    profile = models.ForeignKey(
        to=AccountUser,
        related_name='sellers',
        on_delete=models.DO_NOTHING,
    )

