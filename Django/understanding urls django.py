"""models.py"""
class Page(models.Model):
	nama = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200, unique=True)
	publish = models.BooleanField(default=True, help_text='Status Publish Page.')
	created = models.DateTimeField(auto_now_add=True)
	body = RichTextUploadingField()

	def __unicode__(self):
		return self.nama

	def get_absolute_url(self):
		return reverse("page_detail", kwargs={"slug": self.slug})

"""views.py"""
class PageDetail(generic.DetailView):
    model = models.Page
    template_name = "pages.html"


"""urls.py"""
from . import views
urlpatterns = [
  ...,
	url(r'^page/(?P<slug>\S+)/$', views.PageDetail.as_view(), name="page_detail"),
]

"""templates/page.html"""
{% extends 'base.html' %}
{% block content %}
	<div class="page-detail">
		<h2>
			<a href="{% url "page_detail" slug=object.slug %}">{{ object.nama }}</a>
		</h2>
		<p class="meta-item">
		  <span class="glyphicon glyphicon-calendar" aria-hidden="true"></span> {{ object.created }}
		</p>
		{{ object.body|safe }}
	</div>
{% endblock %}

"""
function "get_absolute_url(self):" in "models.py" has reserve with name "page_detail" and with adding kwargs is "slug". 
So, in your "urls.py", put name of "slug" from your "models.py" and with 'name="page_detail"'.
And then, in your templates you can call with: {% url "page_detail" slug=object.slug %}
"""
