from django import forms

from fMarket.mixins import PlaceholderMixin
from products.models import Product


class BaseProductForm(PlaceholderMixin, forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('owner', 'seller', 'date_created')


class ProductCreateForm(BaseProductForm):
    pass


class ProductUpdateForm(BaseProductForm):
    pass
