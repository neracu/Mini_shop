from django.shortcuts import render, HttpResponse


def index(request):
    context = {
        'title': 'HOME - Главная',
        'content': 'Магазин мебели HOME'
    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'HOME - О нас',
        'content': 'О нас',
        'text_on_page': 'Магазин мебели HOME - это магазин, который продает мебель для дома. '
    }

    return render(request, 'main/about.html', context)

