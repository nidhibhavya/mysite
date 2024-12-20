# accounts/urls.py
from django.urls import path
from .views import signup_view, login_view, custom_logout_view

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', custom_logout_view, name='logout'),  # Use custom logout view
]
