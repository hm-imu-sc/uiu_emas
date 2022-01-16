from django import template

register = template.Library()

@register.filter
def abstractify(value, lenght):
    abs_value = ""
    if len(value) <= lenght:
        return value
    for i in range(lenght - 4):
        abs_value += value[i]
    return f"{abs_value} ..."