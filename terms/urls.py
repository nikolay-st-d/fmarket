from django.urls import path
from terms.views import TermsListView

urlpatterns = [
    path('', TermsListView.as_view(), name='terms')
]