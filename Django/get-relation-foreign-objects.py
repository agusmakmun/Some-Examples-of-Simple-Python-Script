#https://docs.djangoproject.com/en/dev/topics/db/queries/#caching-and-querysets

class Data_Toko(models.Model):
  ....

class Pengiriman(models.Model):
	property = models.ForeignKey(Data_Toko, related_name='pengiriman')
	metode_pengiriman = models.CharField(max_length=200, default='JNE', blank=True, null=True, help_text='Isikan Pengiriman yang tersedia, contoh: JNE')


>>> a = Pengiriman.objects.all()
>>> a
[<Pengiriman: Pengiriman object>, <Pengiriman: Pengiriman object>]
>>> 
>>> from appearance.models import Pengiriman
>>> a = Pengiriman.objects.all()
>>> print ([p.metode_pengiriman for p in a])
[u'Tiki', u'Pos Indonesia']
>>> 
