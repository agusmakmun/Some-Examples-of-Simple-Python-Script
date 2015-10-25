#http://stackoverflow.com/a/8094563

class MyModel(models.Model):
    onefield = models.CharField('The field', max_length=100)

class MyModelAdmin(admin.ModelAdmin):
  def has_add_permission(self, request):
    # if there's already an entry, do not allow adding
    count = MyModel.objects.all().count()
    if count == 0:
      return True

    return False
    
    
#--------------------------------
#appereance/models.py
class Data_Toko(models.Model):
	nama_toko = models.CharField(max_length=200, .... )
	nama_kontak = models.CharField(max_length=200, .... )
	nomor_hp = models.CharField(max_length=200, .... )
	email_kontak = models.EmailField(max_length=70, .... )
	pin_bb = models.CharField(max_length=200, .... )
	jam_kerja = models.CharField(max_length=200, .... )
	ym = models.CharField(max_length=200, ... )
	kode_pos = models.CharField(max_length=200, .... )
	alamat_toko = models.TextField(blank=True, .... )

#appereance/admin.py
class AdminData_Toko(admin.ModelAdmin):
	def has_add_permission(self, request):
		count = models.Data_Toko.objects.all().count()
		if count == 0:
			return True
		return False
	inlines = [ Data_BankInline, PengirimanInline ]
	#http://stackoverflow.com/a/1744292
	formfield_overrides = {
        base_model.TextField: {'widget': Textarea(attrs={'rows': 5, 'cols': 82,})},
    }
