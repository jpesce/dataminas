from django import template

register = template.Library()

@register.filter
def int_to_month(month):
    months = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
    return months[month-1]
