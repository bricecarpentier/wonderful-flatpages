from django import template
from ..utils import get_placeholder


register = template.Library()


@register.simple_tag(takes_context=True)
def placeholder(context, name, **kwargs):
    _, content = get_placeholder(context, name, **kwargs)
    return content


@register.assignment_tag(takes_context=True)
def placeholder_as(context, name, **kwargs):
    _, content = get_placeholder(context, name, **kwargs)
    return content
