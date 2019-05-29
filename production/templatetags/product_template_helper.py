import json
import re
from django import template
from django.template.defaultfilters import truncatechars

register = template.Library()


@register.filter
def split_lines(value):
    if '\n' not in value:
        return '<p>%s</p>' % value

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


@register.simple_tag
def normalize_social_link(link, request, title=None, description=None, image=None):
    url_regex = re.compile(r'(\{url\})', re.IGNORECASE)

    if url_regex.search(link):
        protocol = 'https://' if request.is_secure() else 'http://'
        site_url = protocol + request.get_host()
        link = url_regex.sub(site_url + request.get_full_path(), link)

    if title:
        title_regex = re.compile(r'(\{title\})', re.IGNORECASE)

        if title_regex.search(link):
            link = title_regex.sub(title, link)

    if description:
        description_regex = re.compile(r'(\{description\})', re.IGNORECASE)

        if description_regex.search(link):
            link = description_regex.sub(description, link)

    if image:
        image_regex = re.compile(r'(\{image\})', re.IGNORECASE)

        if image_regex.search(link):
            link = image_regex.sub(image.url, link)

    return link


@register.filter
def truncate_chars(text, char_count):
    return truncatechars(text, char_count)
