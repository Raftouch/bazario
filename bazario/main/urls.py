from django.urls import path
from . import views


app_name = 'main'

urlpatterns = [
    path('', views.featured_products, name='featured_products'),
    path('products/', views.product_list, name='product_list'),
    path('products/category/<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('products/<slug:slug>/', views.product_details, name='product_details'),
]