from django.shortcuts import render, get_object_or_404
from .models import Shop, Menu


def shop_list(request):
    shops = Shop.objects.all()
    return render(request, 'shop/shop_list.html', {
        'shops': shops,
    })


def menu_list(request, shop):
    menu = Menu.objects.all()
    return render(request, 'shop/menu_list.html', {
        'menu': menu,
    })


def menu_detail(request, shop, pk):
    menu = get_object_or_404(Menu, pk=pk, shop=shop)
    return render(request, 'shop/menu_detail.html', {
        'menu': menu
    })

