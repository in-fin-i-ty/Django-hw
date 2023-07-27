from django import template

register = template.Library()


@register.filter()
def mymedia(val):
    if val:
        return f"/media/{val}"
    else:
        return 'static/png/NO.png'


@register.filter()
def mydate(val):
    if val is None:
        return 'Неизвестно'
    else:
        return val
