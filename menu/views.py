from django.shortcuts import render


def menu_view(request, name='Главное_меню'):
    return render(request, './base.html', {'name': name})
