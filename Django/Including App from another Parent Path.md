Example in this problem using wagtail.<br />
And the problem is, we can't import from another parent path. Example tree of projects.
```
/project/
________/manage/
_______________/admin.py
_______________/models.py
________/apps/
________/blog/
_____________/admin.py
_____________/models.py
________....
________/manage.py
```

We need import class from file of `/project/blog/models.py` in my `/project/manage/models.py`. <br />
So, to solve it, we use module of `sys`, egg: `sys.path.append('../')`.

####Example Script:

```
from __future__ import unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel


class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full")
    ]
    
    #http://stackoverflow.com/a/32641692/3445802
    def get_context(self, request):
    	context = super(HomePage, self).get_context(request)
    	import sys
    	sys.path.append('../')
    	from kbsite.models import BlogPage
    	context['blog_post_list'] = BlogPage.objects.filter(live=True).order_by('-date')
    	return context
```
