from django.shortcuts import render


def index(request):
    context = {
        'title': 'Home - главная',
        'content': 'Главная страница магазина',
    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Home - про нас',
        'content': 'Главная страница магазина',
        'text_on_page': 'Текст тут и он такой себе но блять в будущем я буду специалистом',
    }
    return render(request, 'main/about.html', context)
