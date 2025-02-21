from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product

UserModel = get_user_model()


class Review(models.Model):

    MAX_TEXT_LENGTH = 400

    class RatingChoices(models.TextChoices):
        POSITIVE = 'Positive', 'Positive'
        NEUTRAL = 'Neutral', 'Neutral'
        NEGATIVE = 'Negative', 'Negative'

    rating = models.CharField(
        max_length=8,
        choices=RatingChoices.choices,
        default='Positive',
    )
    text = models.TextField(
        max_length=MAX_TEXT_LENGTH,
        help_text=f'Maximum review length: {MAX_TEXT_LENGTH} characters'
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
    date_created = models.DateField(
        auto_now_add=True,
    )

    def __str__(self):
        return f'{self.product} | {self.owner.profile}'