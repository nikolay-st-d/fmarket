# Generated by Django 5.1.3 on 2024-11-20 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_profile_is_seller'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=models.CharField(blank=True, choices=[('Austria', 'Austria'), ('Belgium', 'Belgium'), ('Bulgaria', 'Bulgaria'), ('Croatia', 'Croatia'), ('Cyprus', 'Republic of Cyprus'), ('Czech Republic', 'Czech Republic'), ('Denmark', 'Denmark'), ('Estonia', 'Estonia'), ('Finland', 'Finland'), ('France', 'France'), ('Germany', 'Germany'), ('Greece', 'Greece'), ('Hungary', 'Hungary'), ('Ireland', 'Ireland'), ('Italy', 'Italy'), ('Latvia', 'Latvia'), ('Lithuania', 'Lithuania'), ('Luxembourg', 'Luxembourg'), ('Malta', 'Malta'), ('Netherlands', 'Netherlands'), ('Poland', 'Poland'), ('Portugal', 'Portugal'), ('Romania', 'Romania'), ('Slovakia', 'Slovakia'), ('Slovenia', 'Slovenia'), ('Spain', 'Spain'), ('Sweden', 'Sweden')], default='Austria', max_length=15, null=True),
        ),
    ]
