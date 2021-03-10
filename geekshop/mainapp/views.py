from django.shortcuts import render

from django.conf import settings

from mainapp.models import Product, ProductCategory


def main(request):
    links_menu = [
        {'href': 'main_new', 'name': 'новинки'},
        {'href': 'main_popular', 'name': 'популярное'},
    ]
    products = Product.objects.all()[:4]
    content = {
        'title': 'Главная',
        'links_menu': links_menu,
        'products': products
    }
    return render(request, 'mainapp/index.html', content)


def products(request, pk=None):
    links_menu = ProductCategory.objects.all()[:4]
    same_products = ProductCategory.objects.all()
    content = {
        'title': 'Товары',
        "links_menu": links_menu,
        'same_products': same_products,

    }
    return render(request, 'mainapp/products.html', content)


def contact(request):
    content = {
        'title': 'Контакты'
    }
    return render(request, 'mainapp/contact.html', content)
