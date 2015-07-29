from django import template
from ..forms import ImageForm
from ..utils import get_image_placeholder


register = template.Library()


@register.simple_tag(takes_context=True)
def image_placeholder(context, name, **kwargs):
    p, content = get_image_placeholder(context, name, **kwargs)
    return content


@register.inclusion_tag('flatpages/image_form.html')
def image_form(next_url):
    return {'form': ImageForm(),
            'next_url': next_url}
