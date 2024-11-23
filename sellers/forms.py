from django import forms
from sellers.models import Seller


class BaseSellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        exclude = ('approved', 'account',)
        # fields = '__all__'


class SellerCreateForm(BaseSellerForm):
    pass


class SellerUpdateForm(BaseSellerForm):
    pass
