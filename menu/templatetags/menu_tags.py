from django import template
from django.utils.html import format_html
from menu.models import Menu

register = template.Library()


@register.simple_tag
def draw_menu(name='head', return_to_main=True, test=False):
    html = ''
    if return_to_main: html = f'<ul class="list-group">{"" if name == "Главное_меню" else "<li class=list-group-item><a href=Главное_меню>Вернуться в главное меню</a></li><br>"}'
    menu_items = Menu.objects.filter(name=name).order_by('parent')
    for item in menu_items:
        if item.children.exists():
            html += f'<li class="list-group-item"><div class="caret caret-down" ><a href={item.url} >{item.name}</div></a>'
            html += f'<ul class="list-group nested {"active" if return_to_main or test else ""}">'
            for i in item.children.all():
                html += draw_menu(name=i.name, return_to_main=False)
        else:
            html += f'<li class="list-group-item"><a href={item.url}>{item.name}</a></li>'

        if item.children.exists():
            html += '</ul></li>'
    if return_to_main: html += '</ul>'
    return format_html(html)
