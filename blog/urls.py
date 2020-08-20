from django.urls import path, include
from . import views

urlpatterns = [
    path('blog/', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about')
 ]
