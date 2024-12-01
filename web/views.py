from django.views import generic as views
from products.models import Product


class HomePageView(views.ListView):
    model = Product
    template_name = 'index.html'

    def get_queryset(self):
        products = Product.objects.all().order_by('-id')[:4]
        return products
