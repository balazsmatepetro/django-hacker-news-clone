from django import template
from django.utils.dateformat import format
from django.template.exceptions import TemplateSyntaxError

register = template.Library()


@register.filter(name='shorten_number')
def shorten_number(value: int, max_value: int):
    if not isinstance(max_value, int):
        raise TemplateSyntaxError('The \'max_value\' argument must be an integer!')

    if value > max_value:
        return f'{max_value}+'
    else:
        return value


@register.filter(name='html_datetime')
def html_datetime(value):
    return f"{format(value, 'Y-m-d')}T{format(value, 'H:i:s')}"
