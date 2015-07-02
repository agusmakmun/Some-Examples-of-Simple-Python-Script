--------- views.py ---------
from django.template import loader, Context
from django.db.models import Q

def search(request):
    query = request.GET['q']
    t = loader.get_template('result.html')
    results = Entry.objects.filter(Q(title__icontains=query) | Q(body__icontains=query)).order_by('created')
    c = Context({ 'query': query, 'results':results })
    return HttpResponse(t.render(c))


--------- urls.py
from .views import search
url(r'^results/$', search, name='search'),


--------- base.html --------
<form method="get" action="/results/" class="navbar-form navbar-right" role="search">
  <div class="form-group">
    {% csrf_token %}
    <input type="text" name="q" class="form-control" placeholder="Search" />
  </div>
  <button type="submit" class="btn btn-danger"><span class="glyphicon glyphicon-search" aria-hidden="true"></span></button>
</form>



--------- result.html ---------
{% extends "base.html" %}
{% block title %}Result of - {{ query }} {% endblock %}
{% block canonical_url %}{{ block.super }}/sitemap/{% endblock %}

{% load django_markdown %}
{% block blog_entries %}
  <div class="post">
    <h2>Result of {{ query }}</h2>
    {% if results %}
      {% for object in results %}
        <div class="post">
          <h2><a href="{% url "entry_detail" slug=object.slug %}">{{ object.title }}</a></h2>
          <p class="meta">
            <!-- <span class="glyphicon glyphicon-calendar" aria-hidden="true"></span> --> Date: {{ object.created }} - 
            <!-- <span class="glyphicon glyphicon-user" aria-hidden="true"></span> --> By: {{ object.author }} - 
            <!--<span class="glyphicon glyphicon-tags" aria-hidden="true"></span> --> Tagged under: {{  object.tags.all|join:", " }}
          </p>
          {{ object.body|markdown|safe|truncatewords:"20"|linebreaks }}
          <span style="float:right"><a href="{% url "entry_detail" slug=object.slug %}">Read More..</a></span>
          <div style="clear:both;border-bottom: 1px solid #F2F2F2;margin: 10px 0"></div>
          <!-- http://stackoverflow.com/a/12775861/3445802 -->
        </div>
      {% endfor %}
    {% else %}
      <p>No results.</p>
    {% endif %}
  </div>
{% endblock %}


