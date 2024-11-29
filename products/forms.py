from django import forms
from products.models import Product


class BaseProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('owner', 'seller', 'date_created')


class ProductCreateForm(BaseProductForm):
    pass


class ProductUpdateForm(BaseProductForm):
    pass
