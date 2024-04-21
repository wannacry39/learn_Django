from django.shortcuts import render
from goods.models import Categories, Products

# Create your views here.


def catalog(request):

    categories = Categories.objects.all()
    goods = Products.objects.all()

    context = {
        "title": "Catalog",
        "goods": goods,
        "categories": categories
    }
    return render(request, 'goods/catalog.html', context)


def product(request):
    return render(request, 'goods/product.html')