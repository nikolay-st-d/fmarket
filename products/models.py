from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from sellers.models import Seller

UserModel = get_user_model()


class Product(models.Model):
    NAME_MIN_LENGTH = 3
    NAME_MAX_LENGTH = 40
    DESCRIPTION_MIN_LENGTH = 60

    class QtyUnits(models.TextChoices):
        TON = 'Ton', 'Ton'
        KG = 'Kg', 'Kilogram'
        GR = 'Gram', 'Gram'
        LTR = 'Liter', 'Liter'
        PCS = 'Pc', 'Piece'
        PACK = 'Pack', 'Package'

    class ProductCategories(models.TextChoices):
        VEGETABLES = 'Vegetables', 'Vegetables',
        FRUITS = 'Fruits', 'Fruits',
        NUTS = 'Nuts', 'Nuts'
        CANNED = 'Canned Food', 'Canned Food'
        DRIED = 'Dried Food', 'Dried Food'
        SPICES = 'Spices', 'Spices'
        MEAT = 'Meat Products', 'Meat Products'
        FISH = 'Fish Products', 'Fish Products'
        CHEESE = 'Cheese', 'Cheese'
        MUSHROOMS = 'Mushrooms', 'Mushrooms'

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        validators=[
            MinLengthValidator(NAME_MIN_LENGTH),
        ],
        error_messages={
            MinLengthValidator: f'The name must be at least {NAME_MIN_LENGTH} characters long!'
        }
    )
    description = models.TextField(
        validators=[
            MinLengthValidator(DESCRIPTION_MIN_LENGTH),
        ],
        default='',
        error_messages={
            MinLengthValidator: f'The description must be at least {DESCRIPTION_MIN_LENGTH} characters long!',
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
    photo = models.ImageField(
        upload_to='products/'
    )
    owner = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
    )
    seller = models.ForeignKey(
        to=Seller,
        related_name='products',
        on_delete=models.CASCADE,
    )
    date_created = models.DateField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.name



