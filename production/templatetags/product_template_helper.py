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

