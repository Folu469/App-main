from django.shortcuts import render


# Create your views here.
def catalog(request):
    context = {
        'title': 'Home - каталог',
    }
    return render(request, 'goods/index.html', context)


def product(request):
    context = {'title': 'товар'}
    return render(request, 'goods/product.html', context)
