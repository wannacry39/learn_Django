from django.shortcuts import render
from goods.models import Categories

# Create your views here.


def catalog(request):

    categories = Categories.objects.all()

    context = {
        "title": "Catalog",
        "goods": [
            {
                'image': 'images/goods-imgs/iphone15.webp',
                'name' : 'IPhone 15',
                'price' : '100000'
            },
            {
                'image': 'images/goods-imgs/iphone15.webp',
                'name' : 'IPhone 15',
                'price' : '100000'
            },
            {
                'image': 'images/goods-imgs/iphone15.webp',
                'name' : 'IPhone 15',
                'price' : '100000'
            },
            {
                'image': 'images/goods-imgs/iphone15.webp',
                'name' : 'IPhone 15',
                'price' : '100000'
            },
            {
                'image': 'images/goods-imgs/iphone15.webp',
                'name' : 'IPhone 15',
                'price' : '100000'
            },
            {
                'image': 'images/goods-imgs/iphone15.webp',
                'name' : 'IPhone 15',
                'price' : '100000'
            },
            {
                'image': 'images/goods-imgs/iphone15.webp',
                'name' : 'IPhone 15',
                'price' : '100000'
            },
            {
                'image': 'images/goods-imgs/iphone15.webp',
                'name' : 'IPhone 15',
                'price' : '100000'
            },
            {
                'image': 'images/goods-imgs/iphone15.webp',
                'name' : 'IPhone 15',
                'price' : '100000'
            },
            

        ],
        "categories": categories
    }
    return render(request, 'goods/catalog.html', context)


def product(request):
    return render(request, 'goods/product.html')