from django.http import HttpResponse
from django.views.generic.base import RedirectView
from django.core.urlresolvers import reverse

def pool_fix(request, pk):
    return HttpResponse("You're looking at question %s." % pk)

#Ref: http://stackoverflow.com/a/16627830/3445802
class UserRedirectView(RedirectView):
    permanent = False
    def get_redirect_url(self, pk):
        pk = ''.join(str(pk).split('/'))
        return reverse('pool_fix', kwargs={'pk': pk})
