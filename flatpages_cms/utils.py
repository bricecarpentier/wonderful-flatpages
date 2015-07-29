from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.staticfiles.storage import staticfiles_storage
from django.utils.safestring import mark_safe

from sorl.thumbnail import get_thumbnail

from flatpages_placeholders.utils import get_placeholder
from .models import Image


DEFAULT_IMAGE = getattr(
    settings,
    'FLATPAGES_PLACEHOLDER_IMAGE',
    'flatpages/placeholder.png')


def get_image_placeholder(context, name, **kwargs):
    default_image = kwargs.pop('default', DEFAULT_IMAGE)
    p, content = get_placeholder(context, name, **kwargs)

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

    if 'geometry' in kwargs:
        # some kwargs are left, assuming in order to call sorl
        source = get_thumbnail(
            image_path,
            kwargs.pop('geometry', ''),
            **kwargs).url
    else:
        source = image_url

    return p, mark_safe('<img src="{}" alt="{}">'.format(
            source,
            alternative_text))
