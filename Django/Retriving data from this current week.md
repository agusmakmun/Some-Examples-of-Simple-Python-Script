###Retriving data from this current week {http://stackoverflow.com/a/9159217/3445802}
<pre>
import datetime
date = datetime.date.today()
start_week = date - datetime.timedelta(date.weekday())
end_week = start_week + datetime.timedelta(7)
entries = Entry.objects.filter(created_at__range=[start_week, end_week])
</pre>

###How to retreive records from past weeks in django, {http://stackoverflow.com/a/12682203/3445802}
I assume what you are looking for are all the entries that belong to the same calendar week of the previous week.
This should do the trick:

<pre>
class Entry(models.Model):
    pub_date = models.DateField([...])
</pre>

To get the objects:

<pre>
from datetime import timedelta
from django.utils import timezone
some_day_last_week = timezone.now().date() - timedelta(days=7)
monday_of_last_week = some_day_last_week - timedelta(days=(some_day_last_week.isocalendar()[2] - 1))
monday_of_this_week = monday_of_last_week + timedelta(days=7)
Entry.objects.filter(created_at__gte=monday_of_last_week, created_at__lt=monday_of_this_week)
</pre>
