#### Old

```html
<!-- Pagination links -->
{% if paginator.total_pages > 1 %}
<div class="pagination">
  {% if paginator.previous_page %}
    <a href="{{ paginator.previous_page_path | prepend: site.baseurl | replace: '//', '/' }}">&laquo; Prev</a>
  {% else %}
    <span>&laquo; Prev</span>
  {% endif %}

  {% for page in (1..paginator.total_pages) %}
    {% if page == paginator.page %}
      <em>{{ page }}</em>
    {% elsif page == 1 %}
      <a href="{{ paginator.previous_page_path | prepend: site.baseurl | replace: '//', '/' }}">{{ page }}</a>
    {% else %}
      <a href="{{ site.paginate_path | prepend: site.baseurl | replace: '//', '/' | replace: ':num', page }}">{{ page }}</a>
    {% endif %}
  {% endfor %}

  {% if paginator.next_page %}
    <a href="{{ paginator.next_page_path | prepend: site.baseurl | replace: '//', '/' }}">Next &raquo;</a>
  {% else %}
    <span>Next &raquo;</span>
  {% endif %}
</div>
{% endif %}
```

#### New

```html
<!-- Pagination links -->
{% if paginator.total_pages > 1 %}
<ul class="pagination">
  {% if paginator.previous_page %}
    <li>
      <a href="{{ paginator.previous_page_path | prepend: site.baseurl | replace: '//', '/' }}">&laquo;</a>
    </li>
  {% else %}
    <li class="disabled"><span aria-hidden="true">&laquo;</span></li>
  {% endif %}

  <li><a href="/">First</a></li>

  {% for page in (1..paginator.total_pages) %}
    {% if page == paginator.page %}
      <li class="active">
         <a>{{ page }}<span class="sr-only">(current)</span></a>
      </li>
    {% elsif page == 1 %}
      <li><a href="/">{{ page }}</a></li>
    {% else %}
      <li>
        <a href="{{ site.paginate_path | prepend: site.baseurl | replace: '//', '/' | replace: ':num', page }}">{{ page }}</a>
      </li>
    {% endif %}
  {% endfor %}

  <li><a href="/page{{ paginator.total_pages }}/">Last</a></li>

  {% if paginator.next_page %}
    <li>
      <a href="{{ paginator.next_page_path | prepend: site.baseurl | replace: '//', '/' }}">&raquo;</a>
    </li>
  {% else %}
    <li class="disabled"><span>&raquo;</span></li>
  {% endif %}
</ul>
{% endif %}
```
