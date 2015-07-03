----- models.py ------
from django.db import models
from django.core.urlresolvers import reverse

class Gallery(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	title = models.CharField(max_length=400, help_text="Enter the title of the file or image")
	image_upload = models.ImageField(upload_to='gallery', null=True, blank=True)
	file_upload = models.FileField(upload_to='files', null=True, blank=True)

	def admin_image(self):
	    if self.image_upload:
	        return '<img height="70" width="125" src="%s"/>' % self.image_upload.url
	    return '<img height="40" width="45" src="/static/asset/icons/file-icon.png"/>'
	admin_image.allow_tags = True

	def __unicode__(self):
	    return self.title

	class Meta:
		verbose_name = "Gallery Entry"
		verbose_name_plural = "Gallery"
		ordering = ["-created"]


----- admin.py ------
from django.contrib import admin
from . import models

from django_markdown.admin import MarkdownModelAdmin
from django_markdown.widgets import AdminMarkdownWidget
from django.db.models import TextField

class GalleryAdmin(MarkdownModelAdmin):
    list_display = ("admin_image", "title", "created")
    prepopulated_fields = {"title": ("title",)}
    # Next line is a workaround for Python 2.x
    formfield_overrides = {TextField: {'widget': AdminMarkdownWidget}}
    
admin.site.register(models.Gallery, GalleryAdmin)
