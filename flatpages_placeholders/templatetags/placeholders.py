from django import template
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe

from ..models import Placeholder

register = template.Library()


@register.simple_tag(takes_context=True)
def placeholder(context, name, tag, *args, **kwargs):
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

    # decide whether to make editable or not
    context['edit'] = True
    editable = context.get('user', None) and \
        context['user'].has_perm('flatpages_placeholders.change_placeholder')
    editing = editable and context.get('edit', False)

    # output
    if not editing:
        return mark_safe(u'<{tag}>{content}</{tag}>'.format(tag=tag, content=p.content))
    else:
        type = kwargs.get('type', 'text')
        url = kwargs.pop('data_url', reverse('placeholder_update', args=[p.pk]))
        rest = ' '.join(['{}="{}"'.format(key.replace('_', '-'), value) for key, value in kwargs.iteritems()])

        d = {'tag': tag,
             'type': type,
             'content': p.content,
             'url': url,
             'rest': rest}

        return mark_safe(u'<{tag} data-name="content" data-pk="1" data-type="{type}" data-url="{url}" {rest}>{content}</{tag}'.format(**d))
