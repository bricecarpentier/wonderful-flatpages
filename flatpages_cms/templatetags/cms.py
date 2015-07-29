from django import template
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.staticfiles.storage import staticfiles_storage
from sorl.thumbnail import get_thumbnail

from flatpages_placeholders.models import Placeholder
from ..models import Image


register = template.Library()

DEFAULT_IMAGE = getattr(
    settings,
    'FLATPAGES_PLACEHOLDER_IMAGE',
    'flatpages/placeholder.png')


@register.simple_tag(takes_context=True)
def image_placeholder(context, name, **kwargs):
    # fetch placeholder content
    page = context.get('flatpage', None)
    page_independent = kwargs.pop('page_independent', False)
    language = kwargs.pop('language', None)
    default_image = kwargs.pop('default', DEFAULT_IMAGE)

    query_dict = {
        'name': '{}{}'.format(name, '_' + language if language is not None else ''),
        'page': page if page and not page_independent else None,
    }

    visible = kwargs.get('visible', None)
    if visible is not None:
        query_dict['visible'] = visible

    p, created = Placeholder.objects.get_or_create(**query_dict)

    try:
        image = Image.objects.get(pk=p.content)
        alternative_text = image.alternative_text
        image_path = image.file.path
        image_url = image.file.url
    except Exception:
        image = None
        alternative_text = ''
        image_path = '{}://{}{}'.format(
            'https' if context['request'].is_secure() else 'http',
            get_current_site(context['request']).domain,
            staticfiles_storage.url(default_image))
        image_url = staticfiles_storage.url(default_image)

    if len(kwargs):
        # some kwargs are left, assuming in order to call sorl
        source = get_thumbnail(
            image_path,
            kwargs.pop('geometry', ''),
            **kwargs).url
    else:
        source = image_url

    return '<img src="{}" alt="{}">'.format(
        source,
        alternative_text)
