# Generated by Django 5.1.4 on 2024-12-10 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0023_alter_product_delivery_alter_product_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='views_count',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
    ]
