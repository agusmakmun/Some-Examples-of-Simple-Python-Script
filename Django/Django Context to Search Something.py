from django.template import loader, Context
from django.db.models import Q
from blog.views import Entry

def search(request):
    query = request.GET['q']
    t = loader.get_template('result.html')
    results = Entry.objects.filter(Q(title__icontains=query) | Q(body__icontains=query))#.order_by('created')
    c = Context({ 'query': query, 'results':results })
    return HttpResponse(t.render(c))

"""
title ==> object title from { models.py }
body ==> object body from { models.py }
"""
