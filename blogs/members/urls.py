from django.urls import path
from .views import RegistrationView, UserEditView, PasswordsChangeView
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('profile/', UserEditView.as_view(), name='edit_profile'),
    path('password/', PasswordsChangeView.as_view(template_name='registration/password_change.html')),
]
