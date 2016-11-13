import re
from django import template
register = template.Library()


@register.filter
def as_rupiah(nominal):
    """
    {% load as_rupiah %}
    {{ nominal|as_rupiah }}
    """
    if type(nominal) is int:
        return re.sub(
            "(\d)(?=(\d{3})+(?!\d))", r"\1.", "%d" % nominal
        )
    return nominal
