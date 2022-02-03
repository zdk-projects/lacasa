from django import template

register = template.Library()


@register.simple_tag
def invert_value(value):
    return value


@register.simple_tag
def split_comma(value):
    value = value.split(',')
    return value


@register.simple_tag
def is_list(val):
    return isinstance(val, list)


register.filter('invert_value', invert_value)
register.filter('split_comma', split_comma)
register.filter('is_list', is_list)
