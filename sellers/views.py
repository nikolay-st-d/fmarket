from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic as views

from sellers.forms import SellerCreateForm, SellerUpdateForm
from sellers.models import Seller


class SellersListView(views.ListView):
    model = Seller
    template_name = 'sellers/sellers.html'
    paginate_by = 4


class SellerDetailsView(LoginRequiredMixin, views.DetailView):
    model = Seller
    template_name = 'sellers/seller-details.html'


class SellerCreateView(LoginRequiredMixin, views.CreateView):
    model = Seller
    form_class = SellerCreateForm
    template_name = 'sellers/seller-create.html'
    success_url = reverse_lazy('index')


class SellerUpdateView(LoginRequiredMixin, views.UpdateView):
    model = Seller
    form_class = SellerUpdateForm
    template_name = 'sellers/seller-update.html'
    success_url = reverse_lazy('index')

