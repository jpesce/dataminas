from django import template

register = template.Library()

@register.filter
def breadcrumb_url(categories, position):
    url = ''
    for category in categories[:position]:
        url += category.name_url+'/'
    return url[:-1] # Remove trailing /
