# Generated by Django 5.1.3 on 2024-11-20 18:01

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='available_qty',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default='', error_messages={django.core.validators.MinLengthValidator: 'The description length must be at least 120 characters!'}, validators=[django.core.validators.MinLengthValidator(120)]),
        ),
        migrations.AddField(
            model_name='product',
            name='min_order',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='product',
            name='owner',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.DO_NOTHING, related_name='products', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='product',
            name='qty_units',
            field=models.CharField(choices=[('Tons', 'Tons'), ('Kg', 'Kilograms'), ('Gram', 'Grams'), ('Liters', 'Liters'), ('Pcs', 'Pieces'), ('Pack', 'Package')], default='Kg', max_length=6),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(error_messages={django.core.validators.MinLengthValidator: 'The name must be at lease 12 characters long!'}, max_length=60, validators=[django.core.validators.MinLengthValidator(12)]),
        ),
    ]
