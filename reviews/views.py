from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic as views

from products.models import Product
from reviews.forms import CreateReviewForm
from reviews.models import Review


class ListReviewsView(LoginRequiredMixin, views.ListView):
    model = Review
    template_name = 'reviews/user-reviews.html'
    paginate_by = 18

    def get_queryset(self):
        return Review.objects.filter(owner=self.request.user).order_by('-date_created',)


class CreateReviewView(LoginRequiredMixin, views.CreateView):
    model = Review
    form_class = CreateReviewForm
    template_name = 'reviews/create-review.html'

    def get_product_pk(self):
        pk = self.request.GET.get('product')
        if pk and pk.isdigit():
            return pk
        return 0

    def form_valid(self, form):
        pk = self.get_product_pk()
        product = get_object_or_404(Product, pk=pk)
        form.instance.product = product
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('product-details', kwargs={'pk': self.request.GET.get('product')})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.get_product_pk()
        product = get_object_or_404(Product, pk=pk)
        context['product_name'] = product.name
        context['product_image'] = product.photo
        context['seller_name'] = product.seller.name
        context['seller_country'] = product.owner.profile.country
        return context


class UpdateReviewView(LoginRequiredMixin, UserPassesTestMixin, views.UpdateView):
    model = Review
    form_class = CreateReviewForm
    template_name = 'reviews/update-review.html'

    def test_func(self):
        review = self.get_object()
        return review.owner == self.request.user

    def get_success_url(self):
        return reverse('product-details', kwargs={'pk': self.object.product.pk})


class DeleteReviewView(LoginRequiredMixin, UserPassesTestMixin, views.DeleteView):
    model = Review
    template_name = 'reviews/delete-review.html'

    def test_func(self):
        review = self.get_object()
        return review.owner == self.request.user

    def get_success_url(self):
        return reverse('product-details', kwargs={'pk': self.object.product.pk})

