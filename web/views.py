from django.views import generic as views
from products.models import Product


class HomePageView(views.ListView):
    HOME_PAGE_LATEST_PRODUCTS_NUMBER = 4
    model = Product
    template_name = 'index.html'

    def get_queryset(self):
        products = Product.objects.all().order_by('-id')[:self.HOME_PAGE_LATEST_PRODUCTS_NUMBER]
        return products
