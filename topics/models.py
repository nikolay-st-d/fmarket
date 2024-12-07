from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Topic(models.Model):
    class CategoryChoices(models.TextChoices):
        ACCOUNTS = 'Accounts', 'Accounts'
        BUYING = 'Buying', 'Buying'
        SELLING = 'Selling', 'Selling'

    category = models.CharField(
        max_length=8,
        choices=CategoryChoices.choices
    )
    title = models.CharField(
        max_length=120,
    )
    description = models.CharField(
        max_length=255,
    )
    body = models.TextField()
    list_order = models.PositiveIntegerField(
        default=0,
    )
    last_updated = models.DateTimeField(
        auto_now=True,
    )
    updated_by = models.ForeignKey(
        to=UserModel,
        on_delete=models.DO_NOTHING,
    )
