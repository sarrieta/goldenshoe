from django import template

register = template.Library()


@register.filter
def display_matches(match, username):
    return username
