from django.views import generic as views
from products.models import Product


class ProductsListView(views.ListView):
    model = Product
    template_name = 'products/products.html'
    paginate_by = 4  # TODO: set this for production


class ProductDetailsView(views.DetailView):
    model = Product
    template_name = 'products/product-details.html'
