from django import template
from django.utils.safestring import mark_safe

from ..models import Placeholder


register = template.Library()


@register.simple_tag(takes_context=True)
def placeholder(context, name, tag, *args, **kwargs):
    """
    """
    # fetch placeholder content
    page = context.get('flatpage', None)
    page_independent = kwargs.get('page_independent', False)

    query_dict = {'name': name}
    if page and not page_independent:
        query_dict['page'] = page

    visible = kwargs.get('visible', None)
    if visible is not None:
        query_dict['visible'] = visible

    p, created = Placeholder.objects.get_or_create(**query_dict)

    return mark_safe(p.content)
