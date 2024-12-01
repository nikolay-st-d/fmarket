from django import forms
from fMarket.mixins import PlaceholderMixin
from sellers.models import Seller


class BaseSellerForm(PlaceholderMixin, forms.ModelForm):
    class Meta:
        model = Seller
        exclude = ('approved', 'account',)


class SellerCreateForm(BaseSellerForm):
    pass


class SellerUpdateForm(BaseSellerForm):
    pass

