from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from django.views import generic as views
from sellers.forms import SellerCreateForm, SellerUpdateForm
from sellers.models import Seller

UserModel = get_user_model()


class SellersListView(views.ListView):
    model = Seller
    template_name = 'sellers/sellers.html'
    ordering = '-pk'
    paginate_by = 4


class SellerDashboardView(LoginRequiredMixin, views.DetailView):
    model = Seller
    template_name = 'sellers/dashboard.html'


class SellerDetailsView(LoginRequiredMixin, views.DetailView):
    model = Seller
    template_name = 'sellers/seller-details.html'


class SellerCreateView(LoginRequiredMixin, views.CreateView):
    model = Seller
    form_class = SellerCreateForm
    template_name = 'sellers/seller-create.html'

    def form_valid(self, form):
        form.instance.account = self.request.user
        form.instance.approved = False
        return super().form_valid(form)

    def get_success_url(self):
        messages.success(self.request, "Seller profile created successfully!")
        return reverse('seller-update', kwargs={'pk': self.object.pk})


class SellerUpdateView(LoginRequiredMixin, UserPassesTestMixin, views.UpdateView):
    model = Seller
    form_class = SellerUpdateForm
    template_name = 'sellers/seller-update.html'

    def test_func(self):
        seller = self.get_object()
        return seller.account == self.request.user

    def get_success_url(self):
        messages.success(self.request, "Seller profile updated successfully!")
        return reverse('seller-update', kwargs={'pk': self.object.pk})


class SellerDeleteView(LoginRequiredMixin, UserPassesTestMixin, views.DeleteView):
    model = Seller
    template_name = 'sellers/seller-delete.html'
    success_url = reverse_lazy('seller-create')

    def test_func(self):
        seller = self.get_object()
        return seller.account == self.request.user


