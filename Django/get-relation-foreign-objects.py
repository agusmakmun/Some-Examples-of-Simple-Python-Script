#https://docs.djangoproject.com/en/dev/topics/db/queries/#caching-and-querysets

#1. Just for one field: metode_pengiriman
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
>>> c = [str(p.metode_pengiriman) for p in a]
>>> c
['Tiki', 'Pos Indonesia']
>>> 
>>> for i in c:
...     print i
... 
Tiki
Pos Indonesia
>>> 



#for much more field:

>>> from appearance.models import Data_Bank
>>> a = Data_Bank.objects.all()
>>> b = [ [p.nama_bank, p.no_rekening, p.pemilik_rekening] for p in a ]
>>> b[0]
[u'BRI', u'12345', u'Summon']
>>> str(b[0][0])
'BRI'
>>> 

>>> from appearance.models import Data_Bank
>>> a = Data_Bank.objects.all()
>>> b = [ [p.nama_bank, p.no_rekening, p.pemilik_rekening] for p in a ]
>>> for i in b:
...     print i[0], i[1], i[2]
... 
BRI 12345 Summon
BNI 0987675 agus
>>> 
