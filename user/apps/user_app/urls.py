from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('',views.index),
    path('user_app/dashboard/',views.dashboard),
    path('login_url/',LoginView.as_view()),
    path('register_url/',views.register),
    path('logout/',LogoutView.as_view(next_page='dashboard')),
]