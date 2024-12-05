from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views import generic as views

from products.models import Product
from reviews.forms import CreateReviewForm
from reviews.models import Review


class CreateReviewView(LoginRequiredMixin, views.CreateView):
    model = Review
    form_class = CreateReviewForm
    template_name = 'reviews/create-review.html'

    def form_valid(self, form):
        product = Product.objects.filter(pk=self.request.GET.get('product')).first()
        form.instance.product = product
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('product-details', kwargs={'pk': self.request.GET.get('product')})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = Product.objects.filter(pk=self.request.GET.get('product')).first()
        context['product_name'] = product.name
        context['product_image'] = product.photo
        context['seller_name'] = product.seller.name
        return context


class UpdateReviewView(LoginRequiredMixin, views.UpdateView):
    model = Review
    form_class = CreateReviewForm
    template_name = 'reviews/update-review.html'

    def get_success_url(self):
        return reverse('product-details', kwargs={'pk': self.object.product.pk})


class DeleteReviewView(LoginRequiredMixin, views.DeleteView):
    model = Review
    template_name = 'reviews/delete-review.html'

    def get_success_url(self):
        return reverse('product-details', kwargs={'pk': self.object.product.pk})

