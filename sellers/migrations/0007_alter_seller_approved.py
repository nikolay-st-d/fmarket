# Generated by Django 5.1.3 on 2024-11-22 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellers', '0006_alter_seller_address_alter_seller_contact_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]