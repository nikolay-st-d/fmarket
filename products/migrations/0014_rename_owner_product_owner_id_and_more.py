# Generated by Django 5.1.3 on 2024-11-26 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_alter_product_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='owner',
            new_name='owner_id',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='seller',
            new_name='seller_id',
        ),
    ]
