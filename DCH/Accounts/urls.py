from django.urls import path
from .views import RegistrationView, LoginView, LogoutView

urlpatterns = [
    path('login/', LoginView, name='accounts_login'),
    path('logout/', LogoutView, name='accounts_logout'),
    path('registration/', RegistrationView, name='accounts_registration'),
]