from django.urls import path
from . import views


app_name = 'main'

urlpatterns = [
    path('', views.featured_products, name='featured_products'),
    path('<slug:slug>/', views.product_details, name='product_details'),
]