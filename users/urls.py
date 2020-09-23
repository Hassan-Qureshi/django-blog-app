from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('auth/register/', views.register, name='sign-up'),
    path('auth/login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='log-in'),
    path('auth/logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='log-out'),
    # Request to Reset the user password
    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),
         name='password_reset'),
    # Reset the user password Confirmation Page in which django needs uidb and token for security purpose
    path('password-reset-done/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),

    # This route is to tell user that the reset password email has been sent to your email check your mail box. :)
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),

    path('profile/', views.profile, name='profile'),

]
