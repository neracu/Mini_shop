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


def delivery(request):
    context = {
        'title': 'Доставка и оплата',
        'content': 'Можем доставить, а вы можете оплатить',
        'text_on_page': 'Доставка в любую точку мира'
    }

    return render(request, 'main/delivery.html', context)


def contacts(request):
    context = {
        'title': 'Наши контакты',
        'content': 'Контакты',
        'text_on_page': 'Номер: +88005553535'
    }

    return render(request, 'main/contacts.html', context)

