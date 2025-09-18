import json
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name='json')
def json_filter(value):
    """
    Converts a Python dictionary or object to a formatted JSON string.
    """
    if not isinstance(value, dict):
        return value
        
    json_str = json.dumps(value, indent=4)
    return mark_safe(json_str)

