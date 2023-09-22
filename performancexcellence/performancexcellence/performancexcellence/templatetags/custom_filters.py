from django import template

register = template.Library()

@register.filter
def remove_static(value):
    return value.replace('static/', '', 1)
