from django.contrib.auth import get_user_model
from django.views import generic as views

from products.models import Product
from sellers.models import Seller

UserModel = get_user_model()


class HomePageView(views.TemplateView):
    template_name = 'index.html'
