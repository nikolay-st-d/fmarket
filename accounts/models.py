
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.core.validators import MinLengthValidator
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.db import models
from accounts.managers import AccountUserManager


class AccountUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
        error_messages={
            'unique': _('User with this email already exists!'),
        }
    )
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    USERNAME_FIELD = 'email'
    objects = AccountUserManager()


class Profile(models.Model):
    class EUCountries(models.TextChoices):
        AUSTRIA = 'AT', 'Austria'
        BELGIUM = 'BE', 'Belgium'
        BULGARIA = 'BG', 'Bulgaria'
        CROATIA = 'HR', 'Croatia'
        REPUBLIC_OF_CYPRUS = 'CY', 'Republic of Cyprus'
        CZECH_REPUBLIC = 'CZ', 'Czech Republic'
        DENMARK = 'DK', 'Denmark'
        ESTONIA = 'EE', 'Estonia'
        FINLAND = 'FI', 'Finland'
        FRANCE = 'FR', 'France'
        GERMANY = 'DE', 'Germany'
        GREECE = 'GR', 'Greece'
        HUNGARY = 'HU', 'Hungary'
        IRELAND = 'IE', 'Ireland'
        ITALY = 'IT', 'Italy'
        LATVIA = 'LV', 'Latvia'
        LITHUANIA = 'LT', 'Lithuania'
        LUXEMBOURG = 'LU', 'Luxembourg'
        MALTA = 'MT', 'Malta'
        NETHERLANDS = 'NL', 'Netherlands'
        POLAND = 'PL', 'Poland'
        PORTUGAL = 'PT', 'Portugal'
        ROMANIA = 'RO', 'Romania'
        SLOVAKIA = 'SK', 'Slovakia'
        SLOVENIA = 'SI', 'Slovenia'
        SPAIN = 'ES', 'Spain'
        SWEDEN = 'SE', 'Sweden'

    user = models.OneToOneField(
        to=AccountUser,
        on_delete=models.DO_NOTHING,
        primary_key=True,
    )
    first_name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        help_text='First Name'
    )
    last_name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )
    country = models.CharField(
        max_length=2,
        choices=EUCountries.choices,
        default=EUCountries.AUSTRIA,
    )
    phone_number = models.CharField(
        max_length=16,
        validators=(
            MinLengthValidator(8),
        ),
        null=True,
        blank=True,
    )
