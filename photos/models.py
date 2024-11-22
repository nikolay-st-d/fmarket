from django.core.validators import MinLengthValidator
from django.db import models

from accounts.models import AccountUser
from products.models import Product


class ProductPhoto(models.Model):

    name = models.CharField(
        max_length=60,
        validators=[
            MinLengthValidator(6)
        ],
    )
    image = models.ImageField(
        upload_to='product_photos/'
    )
    product = models.ForeignKey(
        to=Product,
        related_name='photos',
        on_delete=models.CASCADE,
    )
    owner = models.ForeignKey(
        to=AccountUser,
        related_name='photos',
        on_delete=models.DO_NOTHING,
    )

