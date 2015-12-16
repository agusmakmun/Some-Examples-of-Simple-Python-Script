"""This just my documentation for problem of `django inlineformset_factory add remove`."""
Refference, Thanks so much:
#http://blog.stanisla.us/2009/10/10/jquery-plugin-django-dynamic-formset/
#http://blog.stanisla.us/2009/10/10/jquery-plugin-django-dynamic-formset/#comment-17

#------------------models.py--------------------
class Transaksi(models.Model):
	"""Detail Produk dan Member"""
	member 		= models.ForeignKey(User, related_name="transaksi_user_affiliate")

	"""Tanggal Publish"""
	publish 	= models.BooleanField(default=True)
	created 	= models.DateField(default=timezone.now)
	modified 	= models.DateTimeField(auto_now=True)

	objects = TransaksiQuerySet.as_manager()
	
	def __unicode__(self):
		return self.nama_pemilik_rekening

	def get_absolute_url(self):
		return reverse("detail_transaksi", kwargs={"slug": self.pk})

	class Meta:
		verbose_name = "Detail Transaksi"
		verbose_name_plural = "Transaksi"
		ordering = ["-created"]

class Buku(models.Model):
	transaksi = models.ForeignKey(Transaksi, related_name='buku')
	nama_buku 	= models.CharField(max_length=200, null=True)
	jumlah_buku	= models.IntegerField(null=True, default=1)

	def __unicode__(self):
		return self.nama_buku

class Foto_Bukti_Pembayaran(models.Model):
	transaksi = models.ForeignKey(Transaksi, related_name='data_bank_member')
	foto_bukti_pembayaran = models.ImageField(upload_to='images/foto_bukti_pembayaran/%Y/%m/%d', null=True, blank=True)
	
	def __unicode__(self):
		return self.foto_bukti_pembayaran.name


#------------------forms.py-------------------------
from django import forms
from django.utils.translation import ugettext_lazy as _

from django.forms import modelformset_factory
from django.forms.models import inlineformset_factory

from .models import Transaksi
from .models import Buku
from .models import Foto_Bukti_Pembayaran

class TransaksiForm(forms.ModelForm):
	class Meta:
		model = Transaksi
		fields = '__all__'

class BukuForm(forms.ModelForm):
	class Meta:
		model = Buku
		fields = ['transaksi', 'nama_buku', 'jumlah_buku']

class Foto_Bukti_PembayaranForm(forms.ModelForm):
	class Meta:
		model = Foto_Bukti_Pembayaran
		fields = ['transaksi', 'foto_bukti_pembayaran']


#----------------views.py--------------------
from . import models
from django.shortcuts import render_to_response

from django.contrib.auth.models import User
from django.core.context_processors import csrf
import datetime, time

"""Form"""
from django.forms.models import inlineformset_factory
from form_transaksi_member import TransaksiForm
from form_transaksi_member import BukuForm
from form_transaksi_member import Foto_Bukti_PembayaranForm

class TransaksiViews(object):
	def new_transaksi_member(self, request):
		if request.user.is_anonymous():
			return HttpResponseRedirect('/accounts/login')
		
		BukuFormSet = inlineformset_factory(models.Transaksi, models.Buku, form=BukuForm, extra=1)
		FotoFormSet = inlineformset_factory(models.Transaksi, models.Foto_Bukti_Pembayaran, form=Foto_Bukti_PembayaranForm, extra=1)
		transaksi = models.Transaksi()

		if request.method == 'GET':
			form = TransaksiForm(instance=transaksi)
			formset_buku = BukuFormSet(instance=transaksi)
			formset_foto = FotoFormSet(instance=transaksi)
		else:
			form = TransaksiForm(request.POST, request.FILES, instance=transaksi)
			formset_buku = BukuFormSet(request.POST, request.FILES, instance=transaksi)
			formset_foto = FotoFormSet(request.POST, request.FILES, instance=transaksi)

			if form.is_valid() and formset_buku.is_valid() and formset_foto.is_valid():
				form.save()
				formset_buku.save()
				formset_foto.save()

				success_msg = "Transaksi Berhasil Dibuat!"
				args = {
						'user': request.user, 
						'new_transaksi_member_form': form, 
						'formset_buku': formset_buku,
						'formset_foto': formset_foto,
						'request': request, 
						'success_msg': success_msg
						}
				args.update(csrf(request))
				args['form'] = form
				return render_to_response('new_transaksi_member.html', args)
		
		args = {
				'user': request.user, 
				'new_transaksi_member_form': form, 
				'formset_buku': formset_buku,
				'formset_foto': formset_foto,
				'request': request
				}
		args.update(csrf(request))
		args['form'] = form
		return render_to_response('new_transaksi_member.html', args)



#-----------templates/add-transaksi.html------------------
{% extends "dashboard_member.html" %}
{% block title %}New Transaksi Member Affiliate - Penerbit PQS{% endblock %}

{% block content_dashboard %}
<script src="/static/assets/js/jquery.js"></script>
<script src="/static/assets/js/formset.min.js"></script>
<style type="text/css">
    .add-row {
        padding-left:18px;
        background:url(/static/assets/icons/add.png) no-repeat left center;
    }
    .delete-row {
        float:right;
        display:block;
        margin-left:4px;
        padding-left:18px;
        background:url(/static/assets/icons/delete.png) no-repeat left center;
    }
    .dynamic-event-form th {
        text-align:right;
        font-weight:bold;
    }
    .dynamic-event-form td span img {
        vertical-align:middle;
        border:0;
    }
</style>


<script type="text/javascript">
    $(function() {
        $(".inline.{{ formset_buku.prefix }}").formset({
            prefix: "{{ formset_buku.prefix }}",
            formCssClass: 'dynamic-formset1'
        })
        $(".inline.{{ formset_foto.prefix }}").formset({
            prefix: "{{ formset_foto.prefix }}",
            formCssClass: 'dynamic-formset2'
        })
    })
</script>

	{% if user.is_authenticated %}
		<form action="." enctype="multipart/form-data" method="post">
		{% csrf_token %}
		{{ new_transaksi_member_form.as_p }}

		<fieldset class='fieldset'>
        <legend>Buku</legend>
		    {{ formset_buku.management_form }}
	    	{{ formset_buku.non_form_errors }}
        {% for form in formset_buku %}
            {{ form.id }}
            <div class="inline {{ formset_buku.prefix }}" id="book-{{ forloop.counter0 }}">
                {{ form }}
            </div>
        {% endfor %}
		</fieldset>
		
		<fieldset class='fieldset'>
        <legend>Foto Bukti Pembayaran</legend>
		    {{ formset_foto.management_form }}
		    {{ formset_foto.non_form_errors }}
 		    {% for form in formset_foto.forms %}
            {{ form.id }}
            <div class="inline {{ formset_foto.prefix }}">
                {{ form }}
            </div>
        {% endfor %}
        </fieldset>

		<button type="submit" class="btn btn-sm form-control btn-success">Submit</button>
		</form>

	{% endif %}
{% endblock %}
