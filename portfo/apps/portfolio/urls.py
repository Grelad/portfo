from django.urls import path

from portfo.apps.portfolio import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('image/<int:pk>', views.ImageDetailView.as_view(), name='image_details'),
    path('add_portfolio/', views.AddPortfolioView.as_view(), name='add_portfolio'),
    path('portfolio/', views.PortfoliosView.as_view(), name='portfolio'),
    path('portfolio/<int:pk>', views.PortfolioDetailView.as_view(), name='portfolio_details'),
    path('add_image/', views.AddImageView.as_view(), name='add_image'),
]
