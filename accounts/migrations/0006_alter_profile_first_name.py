# Generated by Django 5.1.3 on 2024-11-16 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_profile_country_alter_profile_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]