import os
from django.db import models
from django.utils.text import slugify
from accounts.models import AccountUser
from django.utils.translation import gettext_lazy as _

from fMarket.validators import image_size_validator


class Seller(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True,
        error_messages={
            'unique': _('Seller with this name already exists. Please choose another name!'),
        },
        help_text='Farm or farmer name. ',
    )
    description = models.TextField(
        help_text='A brief farm description and you as a farmer.',
    )
    city = models.CharField(
        max_length=40,
        help_text='City or village name the farm is allocated near.',
    )
    address = models.CharField(
        max_length=50,
        help_text='Address of the farm.',
    )
    photo = models.ImageField(
        upload_to='sellers/',
        validators=(image_size_validator,),
        help_text='Photo of yourself.',
    )
    website_url = models.URLField(
        null=True,
        blank=True,
        help_text='Optional. Website URL including https prefix.',
    )
    approved = models.BooleanField(
        default=False
    )
    account = models.ForeignKey(
        to=AccountUser,
        related_name='sellers',
        on_delete=models.CASCADE,
    )

    def save(self, *args, **kwargs):
        existing = None
        if self.pk:
            existing = Seller.objects.filter(pk=self.pk).first()
            if existing and existing.photo and not self.photo:
                self.photo = existing.photo

        if self.photo and (not existing or existing.photo != self.photo):
            ext = os.path.splitext(self.photo.name)[1]
            self.photo.name = f"{slugify(self.name)}{ext}"

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
