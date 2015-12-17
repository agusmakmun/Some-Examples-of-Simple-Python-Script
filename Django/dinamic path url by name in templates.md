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
&lt;li {% if request.get_full_path == &quot;/accounts/transaksi/new/&quot; %}class=&quot;active&quot;{% endif %}&gt;
	&lt;a href=&quot;{% url &quot;new_transaksi_member_page&quot; %}&quot;&gt;
		&lt;span class=&quot;glyphicon glyphicon-plus&quot; aria-hidden=&quot;true&quot;&gt;&lt;/span&gt; Kirim Transaksi
	&lt;/a&gt;
&lt;/li&gt;
</pre>

<b>To:</b> <code>request.resolver_match.url_name</code>

<pre>
&lt;li {% if request.resolver_match.url_name == &quot;new_transaksi_member_page&quot; %}class=&quot;active&quot;{% endif %}&gt;
	&lt;a href=&quot;{% url &quot;new_transaksi_member_page&quot; %}&quot;&gt;
		&lt;span class=&quot;glyphicon glyphicon-plus&quot; aria-hidden=&quot;true&quot;&gt;&lt;/span&gt; Kirim Transaksi
	&lt;/a&gt;
&lt;/li&gt;
</pre>

Refference:
- http://stackoverflow.com/a/27379100/3445802
