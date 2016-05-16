# https://gist.github.com/spout/dc328a5547ec0e37a47f

from django.views.generic.base import TemplateView
from django.template.loader import select_template
from django.template.base import TemplateDoesNotExist
from django.http import Http404


class PageTemplateView(TemplateView):

    def get_template_names(self):
        template_names = []
        slug = self.kwargs.get('slug', 'index')
        if hasattr(self.request, 'LANGUAGE_CODE'):
            template_names += ['pages/%s/%s.html' % (self.request.LANGUAGE_CODE, slug)]
        template_names += ['pages/%s.html' % slug]
        return template_names

    def render_to_response(self, context, **response_kwargs):
        try:
            select_template(self.get_template_names())
        except TemplateDoesNotExist:
            raise Http404
        return super(PageTemplateView, self).render_to_response(context, **response_kwargs)
