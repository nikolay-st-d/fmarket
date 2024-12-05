from django import forms
from fMarket.mixins import PlaceholderMixin
from reviews.models import Review


class BaseReviewForm(PlaceholderMixin, forms.ModelForm):
    class Meta:
        model = Review
        exclude = ('owner', 'product', 'date_created')


class CreateReviewForm(BaseReviewForm):
    pass


class UpdateReviewForm(BaseReviewForm):
    pass
