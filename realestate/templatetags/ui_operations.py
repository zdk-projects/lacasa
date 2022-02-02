from django import template

register = template.Library()


@register.simple_tag
def invert_value(value):
    return value


@register.simple_tag
def split_comma(value):
    print(value)
    value = value.split(',')
    return value


register.filter('invert_value', invert_value)
register.filter('split_comma', split_comma)
