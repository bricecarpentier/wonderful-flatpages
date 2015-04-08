from django import template
from django.utils.safestring import mark_safe

from ..models import Placeholder


register = template.Library()


def get_placeholder_content(context, name, **kwargs):
    """ simply displays the content of a given placeholder
        available keywords:
        - page_independent: The Placeholder is not linked to a page.
                            Useful for header/footer stuff.
                            Defaults to False.
        - visible: the Placeholder is not visible on the page (and thus can't
                   be in-place-edited in a conventional way).
                   Useful for meta keywords and description.
                   Defaults to False.
    """
    # fetch placeholder content
    page = context.get('flatpage', None)
    page_independent = kwargs.get('page_independent', False)
    language = kwargs.get('language', None)

    query_dict = {
        'name': '{}{}'.format(name, '_' + language if language is not None else ''),
        'page': page if page and not page_independent else None,
    }

    visible = kwargs.get('visible', None)
    if visible is not None:
        query_dict['visible'] = visible

    p, created = Placeholder.objects.get_or_create(**query_dict)

    return mark_safe(p.content)


@register.simple_tag(takes_context=True)
def placeholder(context, name, **kwargs):
    return get_placeholder_content(context, name, **kwargs)


@register.assignment_tag(takes_context=True)
def placeholder_as(context, name, **kwargs):
    return get_placeholder_content(context, name, **kwargs)
