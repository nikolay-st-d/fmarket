from django.views import generic as views
from reviews.forms import CreateReviewForm
from reviews.models import Review


class CreateReviewView(views.CreateView):
    model = Review
    form_class = CreateReviewForm
    template_name = 'products/product-details.html'


class DetailsReviewView(views.DetailView):
    model = Review


class UpdateReviewView(views.UpdateView):
    model = Review
    form_class = CreateReviewForm
    template_name = 'products/product-details.html'


class DeleteReviewView(views.DeleteView):
    model = Review
    form_class = CreateReviewForm
    template_name = 'products/product-details.html'

