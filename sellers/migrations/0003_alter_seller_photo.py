# Generated by Django 5.1.3 on 2024-11-21 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellers', '0002_alter_seller_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to='sellers'),
        ),
    ]
