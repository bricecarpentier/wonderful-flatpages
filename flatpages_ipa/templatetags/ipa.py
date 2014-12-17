from django.template import Library


register = Library()


@register.inclusion_tag('flatpages/ipa/assets.html')
def ipa_assets():
    return {}


@register.inclusion_tag('flatpages/ipa/page_trigger.html')
def page_trigger():
    return {}


# add a a filter to add an encapsulating tag that acts as a trigger


# add a filter to set the root tag as a trigger


# add a tag that adds the necessary trigger classes to an element
