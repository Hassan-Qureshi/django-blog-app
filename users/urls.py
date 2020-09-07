from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('auth/register/', views.register, name='sign-up'),
    path('auth/login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='log-in'),
    path('auth/logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='log-out'),
    path('profile/', views.profile, name='profile'),

]
