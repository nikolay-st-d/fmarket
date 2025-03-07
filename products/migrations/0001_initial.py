# Generated by Django 5.1.4 on 2024-12-11 14:47

import django.core.validators
import django.db.models.deletion
import fMarket.validators
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sellers', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(error_messages={django.core.validators.MinLengthValidator: 'The name must be at least 3 characters long!'}, max_length=40, validators=[django.core.validators.MinLengthValidator(3)])),
                ('description', models.TextField(default='', error_messages={django.core.validators.MinLengthValidator: 'The description must be at least 60 characters long!'}, help_text='Minimum length: 60 characters', validators=[django.core.validators.MinLengthValidator(60)])),
                ('category', models.CharField(choices=[('Vegetables', 'Vegetables'), ('Fruits', 'Fruits'), ('Nuts', 'Nuts'), ('Canned Food', 'Canned Food'), ('Dried Food', 'Dried Food'), ('Spices', 'Spices'), ('Meat Products', 'Meat Products'), ('Fish Products', 'Fish Products'), ('Cheese', 'Cheese'), ('Mushrooms', 'Mushrooms'), ('Other', 'Other')], default='Vegetables', max_length=20)),
                ('qty_units', models.CharField(choices=[('Ton', 'Ton'), ('Kg', 'Kilogram'), ('Gram', 'Gram'), ('Liter', 'Liter'), ('Pc', 'Piece'), ('Pack', 'Package')], default='Kg', max_length=6)),
                ('available_qty', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=6, validators=[django.core.validators.MinValueValidator(0)])),
                ('discount', models.PositiveIntegerField(default=0)),
                ('min_order', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)])),
                ('payment', models.CharField(choices=[('Payment on Delivery', 'Payment on Delivery'), ('Cash on Pick-up', 'Cash on Pick-up'), ('PayPal', 'PayPal'), ('Bank Transfer', 'Bank Transfer'), ('Other', 'Other')], default='Payment on Delivery', max_length=30)),
                ('delivery', models.CharField(choices=[('All EU by Courier', 'All EU by Courier'), ('Within Seller Country', 'Within Seller Country'), ('Local Pickup', 'Local Pickup'), ('Other - please ask', 'Other - please ask')], default='Local Pickup', max_length=30)),
                ('photo', models.ImageField(help_text='Recommended image size - min: 800x600, max: 1600x1200', upload_to='products/', validators=[fMarket.validators.image_size_validator])),
                ('date_created', models.DateField(auto_now_add=True)),
                ('views_count', models.PositiveIntegerField(default=0, editable=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='sellers.seller')),
            ],
        ),
    ]
