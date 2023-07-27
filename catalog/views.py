from django.shortcuts import render
from .models import Product, Category


def index(request):
    context = {
        'object_list': Product.objects.all()[:100],
        'title': 'Продукты'
    }
    return render(request, 'main/index.html', context)


def product(request, pk):
    product_item = Product.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(pk=pk),
        'title': f'{product_item.name}'
    }
    return render(request, 'main/product.html', context)


def contacts(request):
    context = {
        'title': 'Контакты'
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"{name} - ({phone}): {message}")
    return render(request, 'main/contacts.html', context)
