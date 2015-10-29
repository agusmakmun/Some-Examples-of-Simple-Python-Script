class Buku(models.Model):
	judul = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200, unique=True)
	cover = models.ImageField(upload_to='covers', null=True, blank=True)
	thumbnail = models.ImageField(upload_to='covers/thumbnail', editable=False)

	def save(self, *args, **kwargs):
		super(Buku, self).save(*args, **kwargs)
		if not self.make_thumbnail():
			raise Exception('Could not create thumbnail - is the file type valid?')

	def make_thumbnail(self):
		from cStringIO import StringIO
		import os
		from django.db import models
		from django.core.files.base import ContentFile
		from django.core.files.storage import default_storage as storage
		from PIL import Image
		
		THUMB_SIZE = (110, 150)

		fh = storage.open(self.cover.name, 'r')
		try:
			image = Image.open(fh)
		except:
			return False
		
		image.thumbnail(THUMB_SIZE, Image.ANTIALIAS)
		fh.close()
		
		thumb_name, thumb_extension = os.path.splitext(self.cover.name)
		thumb_extension = thumb_extension.lower()
		thumb_filename = thumb_name + '_thumb' + thumb_extension

		if thumb_extension in ['.jpg', '.jpeg']:
			FTYPE = 'JPEG'
		elif thumb_extension == '.gif':
			FTYPE = 'GIF'
		elif thumb_extension == '.png':
			FTYPE = 'PNG'
		else:
			return False

		temp_thumb = StringIO()
		image.save(temp_thumb, FTYPE)
		temp_thumb.seek(0)
		self.thumbnail.save(thumb_filename, ContentFile(temp_thumb.read()), save=False)
		temp_thumb.close()

		return True

"""
Problem: 
maximum recursion depth exceeded while calling a Python object.
>>> With: http://stackoverflow.com/a/23927211/3445802

Solved:
>>> self.thumbnail.save(thumb_filename, ContentFile(temp_thumb.read()), save=True)
TO:
>>> self.thumbnail.save(thumb_filename, ContentFile(temp_thumb.read()), save=False)
"""
