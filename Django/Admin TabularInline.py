from django.contrib import admin
from . import models

'''
extra: for add object, 1 is choice max object to add.
max_num: for limit maximum object was added, 3 is choice max limit all object.
'''
class Kategori_Produk_HomeInline(admin.TabularInline):
	model = models.Kategori_Produk_Home
	extra = 1
	max_num = 3 #http://stackoverflow.com/q/30716736/3445802

class AdminBanner_Slider(admin.ModelAdmin):
	def has_add_permission(self, request):
		count = models.Style_Template.objects.all().count()
		if count == 0:
			return True
		return False

	inlines = [ Banner_SliderImageInline, Kategori_Produk_HomeInline ]
	#http://stackoverflow.com/a/1744292
	formfield_overrides = {
        base_model.TextField: {'widget': Textarea(attrs={'rows': 5, 'cols': 82,})},
    }
    
admin.site.register(models.Style_Template, AdminBanner_Slider)
