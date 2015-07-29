from django import template
from sorl.thumbnail import get_thumbnail

from flatpages_placeholders.models import Placeholder
from ..models import Image


register = template.Library()


@register.simple_tag(takes_context=True)
def image_placeholder(context, name, **kwargs):
    # fetch placeholder content
    page = context.get('flatpage', None)
    page_independent = kwargs.pop('page_independent', False)
    language = kwargs.pop('language', None)

    query_dict = {
        'name': '{}{}'.format(name, '_' + language if language is not None else ''),
        'page': page if page and not page_independent else None,
    }

    visible = kwargs.get('visible', None)
    if visible is not None:
        query_dict['visible'] = visible

    p, created = Placeholder.objects.get_or_create(**query_dict)

    image = Image.objects.get(pk=p.content)
    alternative_text = image.alternative_text

    if len(kwargs):
        # some kwargs are left, assuming in order to call sorl
        source = get_thumbnail(
            image.file,
            kwargs.pop('geometry', ''),
            **kwargs).url
    else:
        source = image.file.url

    return '<img src="{}" alt="{}">'.format(
        source,
        alternative_text)
