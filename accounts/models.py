
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

    def save(self, *args, **kwargs):
        is_new_user = self.pk is None
        super().save(*args, **kwargs)
        if is_new_user:
            Profile.objects.create(user=self)


class Profile(models.Model):
    class EUCountries(models.TextChoices):
        AUSTRIA = 'Austria', 'Austria'
        BELGIUM = 'Belgium', 'Belgium'
        BULGARIA = 'Bulgaria', 'Bulgaria'
        CROATIA = 'Croatia', 'Croatia'
        REPUBLIC_OF_CYPRUS = 'Cyprus', 'Republic of Cyprus'
        CZECH_REPUBLIC = 'Czech Republic', 'Czech Republic'
        DENMARK = 'Denmark', 'Denmark'
        ESTONIA = 'Estonia', 'Estonia'
        FINLAND = 'Finland', 'Finland'
        FRANCE = 'France', 'France'
        GERMANY = 'Germany', 'Germany'
        GREECE = 'Greece', 'Greece'
        HUNGARY = 'Hungary', 'Hungary'
        IRELAND = 'Ireland', 'Ireland'
        ITALY = 'Italy', 'Italy'
        LATVIA = 'Latvia', 'Latvia'
        LITHUANIA = 'Lithuania', 'Lithuania'
        LUXEMBOURG = 'Luxembourg', 'Luxembourg'
        MALTA = 'Malta', 'Malta'
        NETHERLANDS = 'Netherlands', 'Netherlands'
        POLAND = 'Poland', 'Poland'
        PORTUGAL = 'Portugal', 'Portugal'
        ROMANIA = 'Romania', 'Romania'
        SLOVAKIA = 'Slovakia', 'Slovakia'
        SLOVENIA = 'Slovenia', 'Slovenia'
        SPAIN = 'Spain', 'Spain'
        SWEDEN = 'Sweden', 'Sweden'

    user = models.OneToOneField(
        to=AccountUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    first_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )
    country = models.CharField(
        max_length=15,
        choices=EUCountries.choices,
        default=EUCountries.AUSTRIA,
        null=True,
        blank=True,
    )
    phone_number = models.CharField(
        max_length=16,
        validators=(
            MinLengthValidator(8),
        ),
        null=True,
        blank=True,
        help_text='Must include the country code, without whitespaces.',
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
