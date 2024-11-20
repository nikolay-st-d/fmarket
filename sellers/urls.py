from django.urls import path
from sellers import views as views

urlpatterns = [
    path('', views.SellersListView.as_view(), name='sellers'),
]