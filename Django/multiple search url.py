#views.py
from django.template import loader, Context
from django.db.models import Q

def search(request):
    query = request.GET['q']
    t = loader.get_template('result.html')
    results = Entry.objects.filter(Q(title__icontains=query) | Q(body__icontains=query))#.order_by('created')
    paginator = Paginator(results, 2) #show 10 articles per page
    page = request.GET.get('page')
    try:
        results = paginator.page(page)
    except PageNotAnInteger:
        results = paginator.page(1)
    except EmptyPage:
        results = paginator.page(paginator.num_pages)

    c = Context({ 'query': query, 'results':results })
    return HttpResponse(t.render(c))

#result.html
<div class="pagination">
    <span class="step-links">
        {% if results.has_previous %}
            <a href="?q={{ query }}&amp;page={{ results.previous_page_number }}"> &laquo; Previous</a>
        {% endif %}

        <span class="current">
            [ Page {{ results.number }} of {{ results.paginator.num_pages }} ]
        </span>

        {% if results.has_next %}
            <a href="?q={{ query }}&amp;page={{ results.next_page_number }}">Next &raquo; </a>
        {% endif %}
    </span>
</div>

"""
http://stackoverflow.com/questions/14959629/django-listview-pagination-using-get-queryset
http://stackoverflow.com/a/14962919

Query parameters must be separated by & not /
/search/?q={{searchq}}/page={{ page_obj.previous_page_number }}

should be:
/search/?q={{searchq}}&page={{ page_obj.previous_page_number }}
Also, it is best practice to use URL resolver instead of hard-coding the url, something like:

{% url 'search' searchq page_obj.previous_page_number %}
"""
