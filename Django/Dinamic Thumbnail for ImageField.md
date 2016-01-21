Dinamic Thumbnail for <code>ImageField</code> worked with <code>Pillow</code>. This available on: https://djangosnippets.org/snippets/10549/

<pre>
import os
from PIL import Image
from cStringIO import StringIO
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage as storage

class DinamicThumbnail(object):
	"""
	param: `self.width` is width of image that will convert to thumbnail.
	param: `self.height` is height of image that will convert to thumbnail.
	param: `self.image_field` is field for models with ImageField, egg: cover = models.ImageField(upload_to='something/')
	param: `self.thumbnail_field` is field for models width ImageField but for thumbnail. egg: thumbnail = models.ImageField(upload_to='something/', editable=False)

	## Output: egg input `summon_agus.png` and then output thumbnail is `summon_agus.png` but different location as you want.

	## Example implementation:
	from dinamic_thumbnail import DinamicThumbnail

	class Product(models.Model):
		cover = models.ImageField(upload_to='images/cover/%Y/%m/%d')
		thumbnail = models.ImageField(upload_to='images/cover/thumbnail/%Y/%m/%d', editable=False)
		.....

		def save(self, *args, **kwargs):
			super(Product, self).save(*args, **kwargs)
			if not DinamicThumbnail(110, 150, self.cover, self.thumbnail).make_thumbnail():
				raise Exception('Could not create thumbnail - is the file type valid?')
	"""

	def __init__(self, width, height, image_field, thumbnail_field):
		self.width		= width
		self.height		= height
		self.image_field		= image_field
		self.thumbnail_field	= thumbnail_field

	def make_thumbnail(self):
		THUMB_SIZE = (self.width, self.height)

		fh = storage.open(self.image_field.name, 'r') 
		try:
			image = Image.open(fh)
		except:
			return False
		
		image.thumbnail(THUMB_SIZE, Image.ANTIALIAS)
		fh.close()

		thumb_name, thumb_extension = os.path.splitext(self.image_field.name)
		thumb_extension = thumb_extension.lower()
		thumb_filename = thumb_name + thumb_extension

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
		self.thumbnail_field.save(thumb_filename, ContentFile(temp_thumb.read()), save=False)
		temp_thumb.close()

		return True
	</pre>
