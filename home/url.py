from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage, name='home'),

    # home account views
    path('register/', views.RegisterView, name='register'),
    path('login/', views.LoginView, name='login'),
    path('logout/', views.LogoutView, name='logout'),
    path('profile/<user_id>/', views.ProfileView, name='profile'),
    path('profile/<user_id>/edit/', views.EditProfileView, name='profile_edit'),

    # Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    # password reset views 
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view( template_name='account/password/password_change_done.html' ), name='password_change_done'),
    path('password_change/', auth_views.PasswordChangeView.as_view( template_name='account/password/password_change.html' ), name='password_change'),
    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view( template_name='account/password/password_reset_done.html' ), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view( template_name= 'account/password/password_reset_form.html' ), name='password_reset'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view( template_name='account/password/password_reset_complete.html' ), name='password_reset_complete'),
]
