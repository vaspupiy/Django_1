import json
import os

from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from mainapp.models import Product, ProductCategory
from geekshop.settings import BASE_DIR


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
    basket = 0
    total = 0
    if request.user.is_authenticated:
        basket = sum(list(Basket.objects.filter(user=request.user).values_list('quantity', flat=True)))
        total_list = list(Basket.objects.filter(user=request.user).values_list('product__price', 'quantity'))
        total = sum([i[0] * i[1] for i in total_list])
    title = 'продукты'
    links_menu = ProductCategory.objects.all()

    if pk is not None:
        if pk == 0:
            products_list = Product.objects.all().order_by('price')
            category_item = {'name': 'все', 'pk': 0}
        else:
            category_item = get_object_or_404(ProductCategory, pk=pk)
            products_list = Product.objects.filter(category=category_item)

        content = {
            'title': title,
            'links_menu': links_menu,
            'category': category_item,
            'products': products_list,
            'basket': basket,
            'total': total
        }

        return render(request, 'mainapp/products_list.html', content)

    same_products = Product.objects.all()[3:6]

    content = {
        'title': title,
        'links_menu': links_menu,
        'same_products': same_products,
        'basket': basket,
        'total': total
    }

    return render(request, 'mainapp/products.html', content)


def contact(request):
    with open(os.path.join(BASE_DIR, 'mainapp/json/contact__locations.json'), 'r', encoding='utf-8') as f:
        locations = json.load(f)
    content = {
        'title': 'Контакты',
        'locations': locations
    }
    return render(request, 'mainapp/contact.html', content)
