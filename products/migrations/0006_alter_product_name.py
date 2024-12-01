# Generated by Django 5.1.3 on 2024-11-21 20:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_product_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(error_messages={django.core.validators.MinLengthValidator: 'The name must be at lease 12 characters long!'}, max_length=30, validators=[django.core.validators.MinLengthValidator(12)]),
        ),
    ]
