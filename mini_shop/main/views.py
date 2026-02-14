from django.shortcuts import render, HttpResponse

from goods.models import Category


def index(request):

    categories = Category.objects.all()

    context = {
        'title': 'HOME - Главная',
        'content': 'Магазин мебели HOME',
        'categories': categories
    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'HOME - О нас',
        'content': 'О нас',
        'text_on_page': 'Магазин мебели HOME - это магазин, который продает мебель для дома. '
    }

    return render(request, 'main/about.html', context)

