from django import template

register = template.Library()


@register.filter
def index(iterable, i):
    return iterable[i]
