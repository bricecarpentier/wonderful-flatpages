from django.template import Library


register = Library()


@register.inclusion_tag('flatpages/ipa/page_trigger.html')
def page_trigger():
    return {}


@register.inclusion_tag('flatpages/ipa/css.html')
def ipa_css():
    return {}


@register.inclusion_tag('flatpages/ipa/js.html')
def ipa_js():
    return {}
