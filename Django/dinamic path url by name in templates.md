<h3>In your urls.py</h3>
<pre>
from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^accounts/transaksi/new/$', views.TransaksiViews().new_transaksi_member, name="new_transaksi_member_page"),
]
</pre>

<h3>In: templates.html</h3>
Change your: <code>request.get_full_path</code>
<pre>
<li {% if request.get_full_path == "/accounts/transaksi/new/" %}class="active"{% endif %}>
	<a href="{% url "new_transaksi_member_page" %}">
		<span class="glyphicon glyphicon-plus" aria-hidden="true"></span> Kirim Transaksi
	</a>
</li>
</pre>

<b>To:</b> <code>request.resolver_match.url_name</code>

<pre>
<li {% if request.resolver_match.url_name == "new_transaksi_member_page" %}class="active"{% endif %}>
	<a href="{% url "new_transaksi_member_page" %}">
		<span class="glyphicon glyphicon-plus" aria-hidden="true"></span> Kirim Transaksi
	</a>
</li>
</pre>

Refference:
- http://stackoverflow.com/a/27379100/3445802
