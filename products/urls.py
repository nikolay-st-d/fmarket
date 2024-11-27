from django.urls import path, include
from products import views as views

urlpatterns = [
    path('', views.ProductsListView.as_view(), name='products'),
    path('create/', views.ProductCreateView.as_view(), name='create-product'),
    path('seller/<int:pk>/', views.SellerProductsView.as_view(), name='seller-products'),
    # path('product/<int:pk>/', views.ProductDetailsView.as_view(), name='product-details'),

    path('product/<int:pk>/', include([
        path('', views.ProductDetailsView.as_view(), name='product-details'),
        path('update/', views.ProductUpdateView.as_view(), name='product-update'),
        path('delete/', views.ProductDeleteView.as_view(), name='product-delete'),
    ]))
]
