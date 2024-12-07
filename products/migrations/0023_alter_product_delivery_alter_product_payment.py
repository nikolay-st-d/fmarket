# Generated by Django 5.1.3 on 2024-12-07 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0022_alter_product_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='delivery',
            field=models.CharField(choices=[('All EU by Courier', 'All EU by Courier'), ('Within Seller Country', 'Within Seller Country'), ('Local Pickup', 'Local Pickup'), ('Other - please ask', 'Other - please ask')], default='Local Pickup', max_length=30),
        ),
        migrations.AlterField(
            model_name='product',
            name='payment',
            field=models.CharField(choices=[('Payment on Delivery', 'Payment on Delivery'), ('Cash on Pick-up', 'Cash on Pick-up'), ('PayPal', 'PayPal'), ('Bank Transfer', 'Bank Transfer'), ('Other', 'Other')], default='Payment on Delivery', max_length=30),
        ),
    ]
