import json
import re
from django import template


register = template.Library()


@register.filter
def split_lines(value):
    if '\n' not in value:
        return value

    regex = re.compile(r'\n')
    divided_lines = re.split(regex, re.sub(r'\r', '', value))

    return ''.join(['<p>%s</p>' % item for item in divided_lines])


@register.filter
def parse_json(value):
    try:
        return json.loads(value)
    except json.JSONDecodeError:
        return []


@register.filter
def get_first_item(array, key):
    return array[0][key]
