http://stackoverflow.com/a/7162816/3445802
# app/templatetags/shuffle.py
import random
from django import template
register = template.Library()

@register.filter
def shuffle(arg):
    tmp = list(arg)[:]
    random.shuffle(tmp)
    return tmp

#Template:
{% load shuffle %}
<ul>
{% for item in list|shuffle %}
    <li>{{ item }}</li>
{% endfor %}
</ul>
