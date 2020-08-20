from django.urls import path, include
from . import views


urlpatterns = [
    path('register/', views.register, name='sign-up'),
    path('login/', views.login, name='log-in'),
 ]
