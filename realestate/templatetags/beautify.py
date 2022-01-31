from django import template

register = template.Library()


@register.filter(name='beautify_phone_number')
def beautify_phone_number(value):
    if len(value) != 14:
        return value
    position_one = value[:4]
    position_one = position_one.replace("00", "+")
    remaining_char = value[4:]

    position_two = remaining_char[:4]

    remaining_char = remaining_char[4:]

    position_three = remaining_char[:4]
    position_four = remaining_char[4:][:4]

    international_format = f"{position_one} {position_two} {position_three} {position_four} "

    return international_format
