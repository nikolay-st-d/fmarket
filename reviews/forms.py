from django import forms
from reviews.models import Review


class BaseReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ('owner', 'product')


class CreateReviewForm(BaseReviewForm):
    pass


class UpdateReviewForm(BaseReviewForm):
    pass

