from django import template

register = template.Library()


@register.simple_tag
def invert_value(value):
    return value


register.filter('invert_value', invert_value)
