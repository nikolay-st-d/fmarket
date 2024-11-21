from django.urls import path, include
from products import views as views

urlpatterns = [
    path('', views.ProductsListView.as_view(), name='products'),
    # path('product/<int:pk>/', views.ProductDetailsView.as_view(), name='product-details'),

    path('product/<int:pk>/', include([
        path('', views.ProductDetailsView.as_view(), name='product-details'),
    ]))
]
