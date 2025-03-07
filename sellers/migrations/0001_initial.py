# Generated by Django 5.1.4 on 2024-12-11 14:47

import django.db.models.deletion
import fMarket.validators
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(error_messages={'unique': 'Seller with this name already exists. Please choose another name!'}, help_text='Farm or farmer name. ', max_length=30, unique=True)),
                ('description', models.TextField(help_text='A brief farm description and you as a farmer.')),
                ('city', models.CharField(help_text='City or village name the farm is allocated near.', max_length=40)),
                ('address', models.CharField(help_text='Address of the farm.', max_length=50)),
                ('photo', models.ImageField(help_text='Photo of yourself.', upload_to='sellers/', validators=[fMarket.validators.image_size_validator])),
                ('website_url', models.URLField(blank=True, help_text='Optional. Website URL including https prefix.', null=True)),
                ('approved', models.BooleanField(default=False)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sellers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
