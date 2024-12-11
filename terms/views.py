from django.views import generic as views
from terms.models import Term


class TermsListView(views.ListView):
    model = Term
    template_name = 'terms/terms.html'

