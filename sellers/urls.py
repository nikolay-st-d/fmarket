from django.urls import path, include
from sellers import views as views

urlpatterns = [
    path('', views.SellersListView.as_view(), name='sellers'),
    path('create/', views.SellerCreateView.as_view(), name='seller-create'),
    path('seller/<int:pk>/', include([
        path('', views.SellerDetailsView.as_view(), name='seller-details'),
        path('update/', views.SellerUpdateView.as_view(), name='seller-update'),
    ]))
]