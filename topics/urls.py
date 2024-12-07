from django.urls import path
from topics import views as views
urlpatterns = [
    path('', views.TopicsListView.as_view(), name='topics'),
    path('create/', views.TopicCreateView.as_view(), name='create-topic'),
    path('<int:pk>/update/', views.TopicUpdateView.as_view(), name='update-topic'),
    path('<int:pk>/delete/', views.TopicDeleteView.as_view(), name='delete-topic'),
    path('<int:pk>/details/', views.TopicDetailsView.as_view(), name='details-topic'),
]
