from django.contrib.auth import views as auth_views
from django.urls import path
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path(
        'login/',
        auth_views.LoginView.as_view(template_name="accounts/login.html", redirect_authenticated_user=True),
        name='login'
    ),
    path('logout/', views.logout_view, name='logout'),
    path(
        'password_reset/',
        auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'),
        name='password_reset'
    ),
]
