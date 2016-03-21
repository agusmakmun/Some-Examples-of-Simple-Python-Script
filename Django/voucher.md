* ASK: https://www.facebook.com/groups/DjangoID/permalink/1293318760682073/
* Bulk Create: http://stackoverflow.com/a/15046740/3445802
* Voucher model

```python
import random
from django.core.exceptions import ObjectDoesNotExist

class Voucher(models.Model):
    value = models.IntegerField(default=0)

class VoucherCode(models.Model):
    code  = models.CharField(max_length=255)
    voucher = models.ForeignKey(Voucher) #IntegerField() #
    value = models.IntegerField()
    start = models.DateTimeField(blank=True,null=True)
    end  = models.DateTimeField(blank=True,null=True)
    status = models.IntegerField(default=0)
    claimed_date = models.DateTimeField(blank=True,null=True)
    #user = models.ForeignKey('signup.User',blank=True,null=True) #IntegerField() #
    generate_key  = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    val = models.IntegerField(null=True,blank=True)

    def save(self,*args,**kwargs):
        try:
            cek = VoucherCode.objects.get(code=self.code)
        except ObjectDoesNotExist:
            ulang = self.val
            i = 0

            while i < ulang:
                kode = ''.join(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(12))
                self.code = kode

                self.value = self.voucher.value
                self.generate_key = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(4))

                super(VoucherCode, self).save(*args, **kwargs)
                i = i+1
  ```

* Voucher admin

```python
class VoucherCodeAdmin(admin.ModelAdmin):
    list_display = ('id','code', 'voucher', 'value', 'start', 
                    'end', 'status', 'claimed_date', #'user', 
                    'generate_key',)
    search_fields = ('code',)
    fields = ('voucher','val',)
```
