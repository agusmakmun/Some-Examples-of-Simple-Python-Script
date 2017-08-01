import os
import base64

def image_as_base64(image_file, format='png'):
    """
    :param `image_file` for the complete path of image.
    :param `format` is format for image, eg: `png` or `jpg`.
    """
    if not os.path.isfile(image_file):
        return None
    
    encoded_string = ''
    with open(image_file, 'rb') as img_f:
        encoded_string = base64.b64encode(img_f.read())
    return 'data:image/%s;base64,%s' % (format, encoded_string)


# Example Usage

from django import models
from django.conf import settings

class Post(models.Model):
    ...
    cover = models.ImageField(upload_to='images/%Y/%m/%d')
    
    def get_cover_base64(self):
        # settings.MEDIA_ROOT = '/path/to/env/projectname/media'
        return image_as_base64(settings.MEDIA_ROOT + self.cover.path)
