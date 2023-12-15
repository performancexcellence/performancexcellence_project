from django import template

register = template.Library()

@register.filter
def remove_static(value):
    return value.replace('static/', '', 1)

@register.filter
def index(sequence, position):
    return sequence[position] if position < len(sequence) else None