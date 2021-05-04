from django.contrib.auth import views as auth_views
from django.urls import path
from portfo.apps.accounts import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='accounts/login.html', redirect_authenticated_user=True),
        name='login'
    ),
    path('profile/', views.EditProfileView.as_view(), name='profile'),
    path('password/', views.PasswordChangeView.as_view(template_name='accounts/password_change.html')),
    path('password_change_success/', views.PasswordChangeView.password_change_success, name='password_change_success'),
    path('delete/', views.EditProfileView.delete_account, name='delete_account')
]
