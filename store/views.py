from django.shortcuts import get_object_or_404, render

from .models import Category, Product


def all_products(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})


def categories(request):
    return {'categories': Category.objects.all()}


def product_detail(request, address):
    product = get_object_or_404(Product, address=address, in_stock=True)
    return render(request, 'store/detail.html', {'product': product})


def category_list(request, category_address):
    category = get_object_or_404(Category, address=category_address)
    products = Product.objects.filter(category=category)
    return render(request, 'store/category.html', {'category': category, 'products': products})
