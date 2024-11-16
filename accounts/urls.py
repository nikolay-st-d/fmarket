from django.urls import path
from accounts.views import LoginUserView, RegisterUserView, LogoutUserView

urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    # path('logout/', UserLogoutView.as_view(), name='user-logout'),
]
