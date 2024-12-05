from django.urls import path
from reviews.views import CreateReviewView, UpdateReviewView, DeleteReviewView

urlpatterns = [
    path('create/', CreateReviewView.as_view(), name="create-review"),
    path('<int:pk>/update/', UpdateReviewView.as_view(), name="update-review"),
    path('<int:pk>/delete/', DeleteReviewView.as_view(), name="delete-review"),

]