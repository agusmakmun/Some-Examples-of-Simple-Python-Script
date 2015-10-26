#Error: Site matching query does not exist.
#Solved: http://stackoverflow.com/a/16068551/3445802

#settinsg.py
SITE_ID = 1
INSTALLED_APPS = (
        ....
        'django.contrib.sites',
)

$> ./manage.py shell
>>> from django.contrib.sites.models import Site
>>> site = Site()
>>> site.domain = 'example.com'
>>> site.name = 'example.com'
>>> site.save()
