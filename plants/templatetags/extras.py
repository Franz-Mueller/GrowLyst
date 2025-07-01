from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


@register.filter
def get_related_field(obj, lookup):
    # e.g. 'strain__name' -> obj.strain.name
    parts = lookup.split("__")
    value = obj
    for part in parts:
        value = getattr(value, part, "")
        if not value:
            return ""
    return value


@register.filter
def attr(obj, attr_name):
    return getattr(obj, attr_name, "")


@register.filter
def getattribute(obj, attr):
    return getattr(obj, attr)
