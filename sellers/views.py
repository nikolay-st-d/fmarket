from django.views import generic as views
from sellers.models import Seller


class SellersListView(views.ListView):
    model = Seller
    template_name = 'sellers/sellers.html'



