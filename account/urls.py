from django.urls import path

from .views import RegisterView, PasswordResetView, PasswordResetConfirmView, PasswordChangeView, ProfileView, UserUpdateView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('reset-password/', PasswordResetView.as_view(), name='reset-password'),
    path('reset-password-confirm/', PasswordResetConfirmView.as_view(),
         name='reset-password-confirm'),
    path('change-password/', PasswordChangeView.as_view(),
         name='change-password/'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('update_profile/', UserUpdateView.as_view(), name='update_profile'),
]
