from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^pool/(?P<pk>[0-9a-zA-Z\/]+)/$', views.UserRedirectView.as_view(), name='pool'),
    url(r'^pool/(?P<pk>[\d\w_]+)$', views.pool_fix, name='pool_fix'), #allow decimal and words only.
]
