from django.contrib.auth.mixins import UserPassesTestMixin
from django.forms import Select, FileInput

from sellers.models import Seller


class PlaceholderMixin:

    def set_placeholder(self):
        for field_name, field in self.fields.items():
            if isinstance(field.widget, (Select, FileInput)):
                continue
            placeholder = field.label or field.name.replace('_', ' ').capitalize()
            if field.help_text:
                placeholder = field.help_text
                field.help_text = ''
            field.widget.attrs['placeholder'] = placeholder

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_placeholder()


class SellerApprovedMixin(UserPassesTestMixin):
    def test_func(self):
        return Seller.objects.filter(account=self.request.user, approved=True).exists()


class StuffOnlyPermissionMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff

