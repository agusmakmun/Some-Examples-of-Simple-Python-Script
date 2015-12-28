Filtering top score for 10 user by transactions.<br />
Thanks to: Sutrisno Efendi, to help this problem.<br />
Asked: http://stackoverflow.com/q/34489680/3445802

Some Refference: 
- http://stackoverflow.com/a/31853259/3445802
- https://docs.djangoproject.com/en/1.8/ref/models/conditional-expressions/#conditional-expressions
- https://docs.djangoproject.com/en/1.9/ref/models/querysets/

###Screenshot Solved
<img src="http://i.imgur.com/o9bUJcC.png">
<img src="http://i.imgur.com/Gx71fnZ.png">

###modles.py
<pre>
class Transaksi(models.Model):
	"""Detail Produk dan Member"""
	member 		= models.ForeignKey(User, related_name="transaksi_user_affiliate")

	"""Data Bank dan Jumlah Transfer"""
	nama_bank_pengirim		= models.CharField(max_length=200, null=True)
	no_rekening_pengirim	= models.CharField(max_length=200, null=True)
	nama_pemilik_rekening	= models.CharField(max_length=200, null=True)
	jumlah_uang_transfer	= models.IntegerField(null=True)
	tanggal_transfer		= models.DateTimeField(default=now_timezone())
</pre>

###views.py
<pre>
	def most_member_transactions(self, request):
		if request.user.is_anonymous():
			return HttpResponseRedirect(URL_MEMBER_LOGIN)

		"""Get Annotation from user, ordered by `10 most user was create transactions`, 
		*) using this some tags get sum of transactions filtering by `user`, this month, this year or another filter: 
		+) templatetags tags: {% load get_sum_transaksi_member %}
			1. {% get_sum_transaksi_user_by_month user_id=member.pk %}	: to see by this month.
			2. {% get_sum_transaksi_user_by_year user_id=member.pk %}	: to see by this year.
			3. {% get_sum_transaksi_user_by_global user_id=member.pk %}	: to see by global transactions.

		from django.db.models import Count, Sum
		from django.contrib.auth.models import User
		
		import time
		MONTH_NOW = time.strftime("%m")
		YEAR_NOW = time.strftime("%Y")

		#filtering 10 top member by most created a transaction in this month.
		top_member_transaksi_by_month = User.objects.filter(transaksi_user_affiliate__created__month=MONTH_NOW, 
													 transaksi_user_affiliate__created__year=YEAR_NOW,
													 transaksi_user_affiliate__publish=True,
													 transaksi_user_affiliate__status_konfirmasi='diterima'
													).annotate(numb_trans=Count('transaksi_user_affiliate__id'))\
													 .order_by('-numb_trans')[:10]

		#filtering 10 top member by most created a transaction in this year.
		top_member_transaksi_by_year = User.objects.filter(transaksi_user_affiliate__created__year=YEAR_NOW,
													transaksi_user_affiliate__publish=True,
													transaksi_user_affiliate__status_konfirmasi='diterima'
													).annotate(numb_trans=Count('transaksi_user_affiliate__id'))\
													 .order_by('-numb_trans')[:10]

		#filtering 10 top member by most created a transaction by global.
		top_member_transaksi_by_global = User.objects.filter(transaksi_user_affiliate__publish=True,
													transaksi_user_affiliate__status_konfirmasi='diterima'
													).annotate(numb_trans=Count('transaksi_user_affiliate__id'))\
													 .order_by('-numb_trans')[:10]

		#filtering 10 top member by most transfer in this month.
		top_member_transfer_by_month = User.objects.filter(transaksi_user_affiliate__created__month=MONTH_NOW, 
													 transaksi_user_affiliate__created__year=YEAR_NOW,
													 transaksi_user_affiliate__publish=True,
													 transaksi_user_affiliate__status_konfirmasi='diterima'
													).annotate(numb_transfer=Sum('transaksi_user_affiliate__jumlah_uang_transfer'))\
													 .order_by('-numb_transfer')[:10]

		#filtering 10 top member by most transfer in this year.
		top_member_transfer_by_year = User.objects.filter(transaksi_user_affiliate__created__year=YEAR_NOW,
													 transaksi_user_affiliate__publish=True,
													 transaksi_user_affiliate__status_konfirmasi='diterima'
													).annotate(numb_transfer=Sum('transaksi_user_affiliate__jumlah_uang_transfer'))\
													 .order_by('-numb_transfer')[:10]

		#filtering 10 top member by most transfer by global transfer.
		top_member_transfer_by_global = User.objects.filter(transaksi_user_affiliate__publish=True,
													 transaksi_user_affiliate__status_konfirmasi='diterima'
													).annotate(numb_transfer=Sum('transaksi_user_affiliate__jumlah_uang_transfer'))\
													 .order_by('-numb_transfer')[:10]
		
		args = {
				'user': request.user,
				'top_member_transaksi_by_month': top_member_transaksi_by_month,
				'top_member_transaksi_by_year': top_member_transaksi_by_year,
				'top_member_transaksi_by_global': top_member_transaksi_by_global,

				'top_member_transfer_by_month': top_member_transfer_by_month,
				'top_member_transfer_by_year': top_member_transfer_by_year,
				'top_member_transfer_by_global': top_member_transfer_by_global,
				}
		return render_to_response('list_most_member_transactions_admin_dashboard.html', args)

</pre>


###templatetags/get_sum_transaksi_member.py
You can set more filter as you need.
<pre>
def set_transaksi_by_month(user_id):
	try:
		user = User.objects.get(pk=user_id)
		return Transaksi.objects.filter(member=user)\
								.filter(publish=True)\
								.filter(created__month=MONTH_NOW)\
								.filter(created__year=YEAR_NOW)\
								.filter(status_konfirmasi='diterima')
	except: pass

"""*) Set Tags 1: For tags by Sum of Transactions"""
@register.simple_tag
def get_sum_transaksi_user_by_month(user_id):
	""" tags: {% get_sum_transaksi_user_by_month user_id=user_affiliate.id %}"""
	return set_transaksi_by_month(user_id).count()
</pre>

###templates/list_most_member_transactions_admin_dashboard.html
You can showing it similar like this.
<pre>
&lt;h3 class=&quot;most_10&quot;&gt;Bulan ini&lt;/h3&gt;
    &lt;table class=&quot;table table-striped table-bordered table-responsive&quot;&gt;
      &lt;thead&gt;
          &lt;tr&gt;
          	&lt;th&gt;Juara&lt;/th&gt;
          	&lt;th&gt;Username&lt;/th&gt;
          	&lt;th&gt;ID Member&lt;/th&gt;
          	&lt;th&gt;Jumlah Transfer&lt;/th&gt;
          &lt;/tr&gt;
      &lt;/thead&gt; 
    	&lt;tbody&gt;
      	{% for member in top_member_transfer_by_month %}
      		&lt;tr&gt;
      			&lt;td&gt;{{ forloop.counter }}&lt;/td&gt;
      			&lt;td&gt;{{ member.username }}&lt;/td&gt;
      			&lt;td&gt;{% load id_transaksi_member %}{% get_id_for_detail_member member_id=member.pk %}&lt;/td&gt;
      			&lt;td&gt;{% load get_sum_transaksi_member %}{% get_sum_transfer_by_month user_id=member.pk %}&lt;/td&gt;
      		&lt;/tr&gt;
      	{% endfor %}
      &lt;/tbody&gt;
    &lt;/table&gt;
</pre>
