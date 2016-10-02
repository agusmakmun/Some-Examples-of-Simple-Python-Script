This config made for https://python.web.id - https://github.com/agusmakmun/Django-Blog-Python-Learning

Inside file of `/yourproject/yourapp/management/commands/autobackup.py`

```python
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'To backup your app!'

    def add_arguments(self, parser):
        parser.add_argument(
            'backup',
            help='To backup your app!'
        )

    def handle(self, *args, **options):
        if options['backup'] == 'yes':
            # Do stuff
            self.stdout.write(self.style.SUCCESS('[+] Successfully backup!'))
        else:
            self.stdout.write(self.style.WARNING('[-] Can not backup!'))
```

**If you work with `hosting`, you can setup on `Cron Jobs`, and setup your time with command:**

```
source /path/to/yourenv/bin/activate && cd /path/to/yourenv/yourproject && ./manage.py autobackup yes
```

**But, if you work with VPS or SERVER, please following this command bellow:**

```
$ sudo crontab -e

# Setup to daily method.
[minute] [hour] [date] [month] [year]

59 23 * * * source /path/to/yourenv/bin/activate && cd /path/to/yourenv/yourproject && ./manage.py autobackup yes
```

**Refferences:**
* http://stackoverflow.com/a/11789141/3445802
* http://stackoverflow.com/a/3287063/6396981

**See alseo:**
* https://docs.djangoproject.com/es/1.9/howto/custom-management-commands/
