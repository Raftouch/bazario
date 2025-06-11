from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def featured_products(request):
    products = Product.objects.filter(available=True)[:3]
    return render(request, 'main/index/index.html', {'products': products})


def product_details(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    return render(request, 'main/product/details.html', {'product': product})