
Reff: http://chase-seibert.github.io/blog/2010/12/10/per-user-timezones-in-django.html

<pre>
import datetime
from django.conf import settings
import pytz

# need to translate to a non-naive timezone, even if timezone == settings.TIME_ZONE, so we can compare two dates
def to_user_timezone(date, profile):
    timezone = profile.timezone if profile.timezone else settings.TIME_ZONE
    return date.replace(tzinfo=pytz.timezone(settings.TIME_ZONE)).astimezone(pytz.timezone(timezone))

def to_system_timezone(date, profile):
    timezone = profile.timezone if profile.timezone else settings.TIME_ZONE
    return date.replace(tzinfo=pytz.timezone(timezone)).astimezone(pytz.timezone(settings.TIME_ZONE))

def now_timezone():
    return datetime.datetime.now().replace(tzinfo=pytz.timezone(settings.TIME_ZONE)).astimezone(pytz.timezone(settings.TIME_ZONE))
</pre>
