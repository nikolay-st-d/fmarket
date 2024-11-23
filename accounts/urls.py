from django.urls import path
from accounts import views as views

urlpatterns = [
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('logout/', views.LogoutUserView.as_view(), name='logout'),
    path('register/', views.RegisterUserView.as_view(), name='register'),
    path('password-change/', views.UserPasswordChangeView.as_view(), name='password-change'),
    path('password-change/done/', views.UserPasswordChangeView.as_view(), name='password_change_done'),
    path('edit/<int:pk>/', views.EditProfileView.as_view(), name='edit-user'),
    path('delete/<int:pk>/', views.DeleteUserView.as_view(), name='delete-account'),
    path('password_reset/', views.UserPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', views.UserPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.UserPasswordResetCompleteView.as_view(), name='password_reset_complete'),

]

'''
accounts/password_reset/ [name='password_reset']
accounts/password_reset/done/ [name='password_reset_done']
accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
accounts/reset/done/ [name='password_reset_complete']
'''