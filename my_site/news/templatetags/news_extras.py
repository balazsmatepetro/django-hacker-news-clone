from django import template
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
