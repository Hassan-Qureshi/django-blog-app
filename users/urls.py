from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register, name='sign-up'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='log-in'),
    path('logout/', auth_views.LoginView.as_view(template_name='users/logout.html'), name='log-out'),
]
