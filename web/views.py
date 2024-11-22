from django.contrib.auth import get_user_model
from django.views import generic as views

from sellers.models import Seller

UserModel = get_user_model()


class HomePageView(views.TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


