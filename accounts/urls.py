from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from accounts import forms

app_name = 'accounts'

urlpatterns = [
    path('register/', views.SignupView.as_view(), name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('login/',
         auth_views.LoginView.as_view(template_name="accounts/login.html", form_class=forms.AuthenticationForm, ),
         name='login'),


]
