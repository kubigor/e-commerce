from django.shortcuts import get_object_or_404, render

from .models import Category, Product


def all_products(request):
    products = Product.objects.filter(is_active=True)
    return render(request, 'store/home.html', {'products': products})


def product_detail(request, address, category_address):
    product = get_object_or_404(Product, address=address, in_stock=True)
    return render(request, 'store/detail.html', {'product': product})


def category_list(request, category_address):
    category = get_object_or_404(Category, address=category_address)
    products = Product.objects.filter(category=category)
    return render(request, 'store/category.html', {'category': category, 'products': products})
