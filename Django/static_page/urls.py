# https://gist.github.com/spout/dc328a5547ec0e37a47f

from django.conf.urls import url
from .views import PageTemplateView

urlpatterns = [
    url(r'^$', PageTemplateView.as_view(), name='index'),
    url(r'^(?P<slug>[-\w\d]+)/$', PageTemplateView.as_view(), name='detail'),
]
