----- views.py -------
def displayAllArticlesUnderTage(request, tag_slug):
    #Entry.objects.filter(~Q(id=1))
    t = loader.get_template('all_tags.html')
    tag = Tag.objects.get(slug = tag_slug)
    articles = Entry.objects.filter(tags = tag.id)
    c = Context({ "articles" : articles, "tag_slug" : tag_slug,})
    return HttpResponse(t.render(c))
    
----- urls.py ----------
url(r'^tag/(?P<tag_slug>\S+)/$', displayAllArticlesUnderTage, name="tag_slug"),

----- all_tags.html ----
{% extends "base.html" %}
{% block title %}Post Under Tag: {{ tag_slug }} {% endblock %}
{% block canonical_url %}{{ block.super }}/tag/{{ tag_slug }}{% endblock %}

{% load django_markdown %}
{% block blog_entries %}
  <div class="post">
    <p class="result-me">Post Under Tag: <i>"{{ tag_slug }}"</i></p>
      {% if tag_slug %}
         {% for obj in articles %}
            <div class="post">
              <h2><a href="{% url "entry_detail" slug=obj.slug %}">{{ obj.title }}</a></h2>
              <p class="meta">
                Date: {{ obj.created }} - 
                By: {{ obj.author }} - 
                Tagged under: {{  obj.tags.all|join:", " }}
              </p>
              {{ obj.body|markdown|safe|truncatewords:"20"|linebreaks }}
              <span style="float:right">
                <a href="{% url "entry_detail" slug=obj.slug %}">Read More..</a>
              </span>
              <div style="clear:both;border-bottom: 1px solid #F2F2F2;margin: 10px 0"></div>
            </div>
         {% endfor %}
      {% endif %}
  </div>
{% endblock %}
