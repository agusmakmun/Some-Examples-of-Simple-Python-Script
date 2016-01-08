####Solved: http://stackoverflow.com/a/2981335/3445802

Check for request.GET variable in the template.
Variables are case-sensitive - so, assuming as lazerscience points out that you actually have the request 
object in the context, you would need to use  <code>{% if request.GET.my_var %}</code>.

egg:
<pre>
{% block pagination %}
	{% if user.is_authenticated %}
		{% if request.GET.filter == 'draft' %}&lt;!-- this like: ?filter=draft --&gt;
			&lt;p class=&quot;alert alert-warning&quot;&gt;
				&lt;span class=&quot;glyphicon glyphicon-info-sign&quot; aria-hidden=&quot;true&quot;&gt;&lt;/span&gt; Pagination disabled in Draft
			&lt;/p&gt;
		{% endif %}
		{% else %}{{ block.super }}
	{% endif %}
{% endblock %}
</pre>
