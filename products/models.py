from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from accounts.models import AccountUser
from sellers.models import Seller


class Product(models.Model):
    NAME_MIN_LENGTH = 12
    NAME_MAX_LENGTH = 40
    DESCRIPTION_MIN_LENGTH = 120

    class QtyUnits(models.TextChoices):
        TON = 'Tons', 'Tons'
        KG = 'Kg', 'Kilograms'
        GR = 'Gram', 'Grams'
        LTR = 'Liters', 'Liters'
        PCS = 'Pcs', 'Pieces'
        PACK = 'Pack', 'Package'

    class ProductCategories(models.TextChoices):
        VEGETABLES = 'Vegetables', 'Vegetables',
        FRUITS = 'Fruits', 'Fruits',
        NUTS = 'Nuts', 'Nuts'
        CANNED = 'Canned Food', 'Canned Food'
        SPICES = 'Spices', 'Spices'
        MEAT = 'Meat Products', 'Meat Products'
        FISH = 'Fish Products', 'Fish Products'
        CHEESE = 'Cheese', 'Cheese'

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        validators=[
            MinLengthValidator(NAME_MIN_LENGTH),
        ],
        error_messages={
            MinLengthValidator: f'The name must be at lease {NAME_MIN_LENGTH} characters long!'
        }
    )
    description = models.TextField(
        validators=[
            MinLengthValidator(DESCRIPTION_MIN_LENGTH),
        ],
        default='',
        error_messages={
            MinLengthValidator: f'The description length must be at least {DESCRIPTION_MIN_LENGTH} characters!',
        }
    )
    category = models.CharField(
        max_length=20,
        choices=ProductCategories.choices,
        default=ProductCategories.VEGETABLES
    )
    qty_units = models.CharField(
        max_length=6,
        choices=QtyUnits.choices,
        default=QtyUnits.KG
    )
    available_qty = models.IntegerField(
        validators=[
            MinValueValidator(0),
        ],
        default=0
    )
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[
            MinValueValidator(0),
        ],
        default=0
    )
    discount = models.PositiveIntegerField(
        default=0
    )
    min_order = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
        ],
        default=1,
    )
    owner = models.ForeignKey(
        to=Seller,
        related_name='products',
        on_delete=models.DO_NOTHING,
    )



