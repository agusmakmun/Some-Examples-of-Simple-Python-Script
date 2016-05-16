from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

import os, time, random, string
from uuid import uuid4

class Upload_File(models.Model):
    title               = models.CharField(max_length=200)
    slug                = models.SlugField(max_length=200, unique=True)
    author              = models.ForeignKey(User, related_name='user')

    def pdf_validator(upload_pdf_obj):
        ext = os.path.splitext(upload_pdf_obj.name)[1]  # [0] = returns path+filename
        valid_extension = ['.pdf']
        if not ext in valid_extension:
            raise ValidationError(u'Unsupported file extension, .pdf only.')

    # Auto rename for field `upload_pdf`
    # Example:
    # - input : This my uploaded file.pdf
    # - output: This-my-uploaded-file_yta26wga3gd156f3215e454d168f6_QqAqbrY.pdf 
    #           - `yta26wga3g` is random string, it will making high scure.
    #           - `d156f3215e454d168f6_QqAqbrY` is uuid4().hex
    # http://stackoverflow.com/a/15141228
    def path_and_rename(path):
        def wrapper(instance, filename):
            ext = filename.split('.')[-1]
            f_name = '-'.join(filename.replace('.pdf', '').split() )
            rand_strings = ''.join( random.choice(string.lowercase+string.digits) for i in range(10) )
            filename = '{}_{}{}.{}'.format(f_name, rand_strings, uuid4().hex, ext)
            return os.path.join(path, filename)
        return wrapper

    # Please comment `validators=[pdf_validator]` before migrate/makemigrations your database.
    # For more: https://docs.djangoproject.com/en/1.9/topics/migrations/#serializing-values
    upload_pdf          = models.FileField(
                                    upload_to=path_and_rename('files/pdf/{}'.format(time.strftime("%Y/%m/%d"))), 
                                    validators=[pdf_validator]
                                    )
