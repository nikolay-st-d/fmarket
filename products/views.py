from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views import generic as views
from products.forms import ProductCreateForm
from products.models import Product
from sellers.models import Seller


class ProductsListView(views.ListView):
    model = Product
    template_name = 'products/products.html'
    ordering = '-id'
    paginate_by = 8


class ProductCreateView(LoginRequiredMixin, views.CreateView):
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


class ProductUpdateView(LoginRequiredMixin, views.UpdateView):
    model = Product
    form_class = ProductCreateForm
    template_name = 'products/product-update.html'

    def get_success_url(self):
        messages.success(self.request, f'Product "{self.object.name}" updated successfully!')
        seller = Seller.objects.get(account=self.request.user)
        return reverse('seller-products', kwargs={'pk': seller.pk})


class ProductDeleteView(views.DeleteView):
    model = Product
    template_name = 'products/product-delete.html'

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
