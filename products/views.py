from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import F
from django.urls import reverse
from django.views import generic as views

from fMarket.mixins import SellerApprovedMixin
from products.forms import ProductCreateForm
from products.models import Product
from sellers.models import Seller


class ProductsListView(views.ListView):
    model = Product
    template_name = 'products/products.html'
    ordering = ('-id',)
    paginate_by = 4


class ProductCreateView(LoginRequiredMixin, SellerApprovedMixin, views.CreateView):
    model = Product
    form_class = ProductCreateForm
    template_name = 'products/product-create.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.seller = Seller.objects.get(account=self.request.user)
        return super().form_valid(form)

    def get_success_url(self):
        messages.success(self.request, f'Product "{self.object.name}" created successfully!')
        seller = Seller.objects.get(account=self.request.user)
        return reverse('seller-products', kwargs={'pk': seller.pk})


class ProductDetailsView(views.DetailView):
    model = Product
    template_name = 'products/product-details.html'

    def get(self, request, *args, **kwargs):
        product_obj = self.get_object()
        Product.objects.filter(pk=product_obj.pk).update(views_count=F('views_count') + 1)
        request.product = product_obj
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = self.object.reviews.all().order_by('-date_created')
        return context


class ProductUpdateView(LoginRequiredMixin, SellerApprovedMixin, views.UpdateView):
    model = Product
    form_class = ProductCreateForm
    template_name = 'products/product-update.html'

    def get_success_url(self):
        messages.success(self.request, f'Product "{self.object.name}" updated successfully!')
        seller = Seller.objects.get(account=self.request.user)
        return reverse('seller-products', kwargs={'pk': seller.pk})


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, views.DeleteView):
    model = Product
    template_name = 'products/product-delete.html'

    def test_func(self):
        product = self.get_object()
        seller = Seller.objects.get(account=self.request.user)
        return product.seller == seller

    def get_success_url(self):
        messages.success(self.request, "Product deleted successfully!")
        seller = Seller.objects.get(account=self.request.user)
        return reverse('seller-products', kwargs={'pk': seller.pk})


class SellerProductsView(LoginRequiredMixin, views.ListView):
    model = Product
    template_name = 'products/seller-products.html'
    paginate_by = 20

    def get_queryset(self):
        return Product.objects.filter(owner=self.request.user).order_by('name')
