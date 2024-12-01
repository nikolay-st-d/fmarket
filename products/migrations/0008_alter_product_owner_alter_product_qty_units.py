# Generated by Django 5.1.3 on 2024-11-23 22:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_product_name'),
        ('sellers', '0012_alter_seller_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='sellers.seller'),
        ),
        migrations.AlterField(
            model_name='product',
            name='qty_units',
            field=models.CharField(choices=[('Ton', 'Ton'), ('Kg', 'Kilogram'), ('Gram', 'Gram'), ('Liter', 'Liter'), ('Pc', 'Piece'), ('Pack', 'Package')], default='Kg', max_length=6),
        ),
    ]
