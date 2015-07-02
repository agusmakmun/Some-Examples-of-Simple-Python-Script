>>> from blog.models import Entry
>>> from django.db.models import Q
>>> Entry.objects.all()
[<Entry: Python ARP Flooding>, <Entry: Bionic Boot>, <Entry: Test Postingan pertama>]
>>> 
>>> Entry.objects.filter(Q(title__icontains="ARP Flooding")).order_by('created')
[<Entry: Python ARP Flooding>]
>>> 
>>> Entry.objects.filter(Q(title__icontains="ARP Flooding") | Q(body__icontains="ARP Flooding")).order_by('created')
[<Entry: Python ARP Flooding>]
>>> 
