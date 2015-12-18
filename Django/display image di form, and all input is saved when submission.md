<h3>Display image di form, and all input is saved when submission</h3>
<p>This method using <code>inlineformset_factory</code><p>

<pre>
&lt;fieldset class=&#39;fieldset&#39;&gt;
&lt;legend class=&quot;alert alert-info&quot;&gt;Foto Bukti Pembayaran&lt;/legend&gt;
{{ formset_foto.management_form }}
{{ formset_foto.non_form_errors }}
	{% for form in formset_foto.forms %}
    {{ form.id }}
    {% if forloop.last %}
    &lt;div class=&quot;inline {{ formset_foto.prefix }}&quot; style=&quot;display:none&quot;&gt;
        {{ form }}
    &lt;/div&gt;
    {% else %}
    &lt;div class=&quot;inline {{ formset_foto.prefix }}&quot;&gt;
        &lt;!-- form: is default --&gt;
        {% for photo in form.visible_fields %}
        	&lt;img src=&quot;/gallery/{{ photo.value }}&quot;&gt;
        {% endfor %}
    &lt;/div&gt;
    {% endif %}
{% endfor %}
&lt;/fieldset&gt;
</pre>
