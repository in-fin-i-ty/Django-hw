from django import template

register = template.Library()


@register.filter()
def mymedia(val, no_val='/static/png/NO.png'):
    if val:
        return f"/media/{val}"

    return no_val


@register.filter()
def mydate(val):
    if val is None:
        return 'Неизвестно'
    else:
        return val
