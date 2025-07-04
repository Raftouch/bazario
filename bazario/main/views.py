from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Category, Product


def home(request):
    products = Product.objects.filter(available=True)[:3]
    return render(request, 'main/index/index.html', {'products': products})


def product_details(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    return render(request, 'main/product/details.html', {'product': product})


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
        
    paginator = Paginator(products, 4)
    page_number = request.GET.get('page', 1)
    
    current_page_products = paginator.page(page_number)

    return render(request, 
                  'main/product/list.html', 
                  {'category': category, 'categories': categories, 'products': current_page_products, 'slug_url': category_slug})