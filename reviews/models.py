from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product

UserModel = get_user_model()


class Review(models.Model):

    class RatingChoices(models.TextChoices):
        NEGATIVE = 'Negative', 'Negative'
        NEUTRAL = 'Neutral', 'Neutral'
        POSITIVE = 'Positive', 'Positive'

    rating = models.CharField(
        max_length=10,
        choices=RatingChoices.choices,
        default='Positive',
    )
    text = models.CharField(
        max_length=255,
        help_text='Maximum review length: 255 characters'
    )
    owner = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    product = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
