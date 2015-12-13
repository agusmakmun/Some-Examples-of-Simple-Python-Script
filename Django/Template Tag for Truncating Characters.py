"""
Refference:
- http://chriskief.com/2014/05/11/django-template-tag-for-truncating-characters-at-a-word-boundary/
- https://github.com/django/django/blob/master/django/template/defaultfilters.py#L16
"""

from django import template
from django.utils.html import strip_tags
from blog.models import Entry, Tag
register = template.Library()
#all_blog_tags = Tag.objects.all()
@register.simple_tag
def blog_tags():
	all_blog_entry = Entry.objects.published()[:5]
	all_blog_entry = [ [p.title, p.slug, p.tags, p.body, p.created ] for p in all_blog_entry ]
	out = []
	for item in all_blog_entry:
		title = str(item[0])
		slug = str(item[1])
		tags = item[2].all()
		tmp_tags_slug = ''
		for tag in tags:
			tmp_tags_slug += str(tag.slug)

		def smart_truncate_chars(value, max_length):
			if len(value) > max_length:
				truncd_val = value[:max_length]
				if value[max_length] != ' ':
					truncd_val = truncd_val[:truncd_val.rfind(' ')]
				return truncd_val + '...'
			return value
		body = smart_truncate_chars(str(item[3].encode('utf-8')), 20) #str(item[3])
		created = str(item[4])
		out.append('%s %s %s %s %s' % (title, slug, tmp_tags_slug, strip_tags(body), created))
	
	return ''.join(out)
