# Generated by Django 5.1.3 on 2024-11-23 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellers', '0012_alter_seller_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='name',
            field=models.CharField(error_messages={'unique': 'Seller with name already exists!'}, max_length=30, unique=True),
        ),
    ]