from django.urls import path
from web.views import HomePageView, ContactView, SuccessView

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('contact/success/', SuccessView.as_view(), name='contact-success'),
]
