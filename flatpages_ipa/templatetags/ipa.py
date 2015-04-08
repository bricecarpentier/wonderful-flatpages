import json

from django.db.models.query import QuerySet
from django.template import Library
from django.core.urlresolvers import reverse
from django.utils.html import escape
from django.utils.safestring import mark_safe

from flatpages_placeholders.models import Placeholder


register = Library()


def is_editing(context):
    context_edit = bool(context['request'].GET.get('edit'))
    editable = context.get('user', None) and \
        context['user'].has_perm('flatpages_placeholders.change_placeholder')
    editing = editable and context_edit

    return editing


@register.assignment_tag(takes_context=True)
def ipa_editing(context):
    return is_editing(context)


@register.inclusion_tag('flatpages/ipa/page_trigger.html', takes_context=True)
def page_trigger(context):
    return {'editing': is_editing(context)}


@register.inclusion_tag('flatpages/ipa/css.html')
def ipa_css():
    return {}


@register.inclusion_tag('flatpages/ipa/js.html')
def ipa_js():
    return {}


@register.simple_tag(takes_context=True)
def ipa_placeholder(context, name, tag, *args, **kwargs):
    """ Outputs the content of a given placeholder, eventually wrapped in a tag
        with x-editable suitable data-* attributes.
        The placeholder will be editable provided the following conditions are met:
        - the user is allowed to modify placeholders
          (has_perm: "flatpages_placeholders.change_placeholder)
        - a "edit" flag is set in the context
        parameters:
        - name: the placeholder's name
        - tag: the wrapping html tag
        available keywords:
        - page_independent: The Placeholder is not linked to a page.
                            Useful for header/footer stuff.
                            Defaults to False.
        - language: The Placeholder's name will be concatenated with
                    the language if specified.
                    Defaults to None
        - visible: the Placeholder is not visible on the page (and thus can't
                   be in-place-edited in a conventional way).
                   Useful for meta keywords and description.
                   Defaults to False.
        - type: the type of editing component to display
        - choices: a list of {value, text} dictionaries to be used as
                   select options
        - data_*: every data_* parameter will be converted to data-* attributes
                  on the html tag

    """
    # fetch placeholder content
    page = context.get('flatpage', None)
    page_independent = kwargs.get('page_independent', False)
    language = kwargs.get('language', None)
    choices = kwargs.pop('choices', None)
    if isinstance(choices, QuerySet):
        choices = [{"value": c.pk, "text": str(c)} for c in list(choices)]

    query_dict = {
        'name': '{}{}'.format(name, '_' + language if language is not None else ''),
        'page': page if page and not page_independent else None,
    }

    visible = kwargs.get('visible', None)
    if visible is not None:
        query_dict['visible'] = visible

    p, created = Placeholder.objects.get_or_create(**query_dict)

    # decide whether to make editable or not
    editing = is_editing(context)
    if choices is None:
        content = p.content
    else:
        d = {c['value']: c['text'] for c in choices}
        content = d[p.content] if p.content in d else p.content

    # output
    if not editing:
        return mark_safe(u'<{tag}>{content}</{tag}>'.format(
            tag=tag,
            content=content))
    else:
        type = kwargs.get('type', 'text')
        url = kwargs.pop('data_url', reverse('placeholder_update', args=[p.pk]))
        rest = ' '.join(['{}="{}"'.format(key.replace('_', '-'), value) for key, value in kwargs.iteritems()])

        d = {'tag': tag,
             'type': type,
             'content': content,
             'url': url,
             'rest': rest,
             'source': ''}
        if choices is not None:
            d['source'] = 'data-source="{}"'.format(escape(json.dumps(choices)))

        return mark_safe(u'<{tag} data-name="content" data-pk="1" data-type="{type}" data-url="{url}" {source} {rest}>{content}</{tag}>'.format(**d))
