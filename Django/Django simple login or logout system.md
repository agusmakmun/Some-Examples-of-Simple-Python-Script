###Django simple login or logout system
Thanks: http://stackoverflow.com/a/14384510/3445802

simple login/logout system could be find here: https://github.com/michaelarshinov/django_simple_backend_user_model
Let me briefly explain how to use standard auth through the user model in Django:

####appname/views.py:
```
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response
from django.template import 

@login_required
def stat_info(request):
return render_to_response('stat_info.html',
  {'is_auth':request.user.is_authenticated()},
  context_instance=RequestContext(request))

@login_required
def mainmenu(request):
return render_to_response('mainmenu.html',{},
  context_instance=RequestContext(request))
```

####urls.py:
```
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    (r'^statinfo/$', 'appname.views.stat_info'),
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page' : '/accounts/login'}),
    (r'^mainmenu/$', 'appname.views.mainmenu')
)
```

####settings.py:
```
...        
LOGIN_REDIRECT_URL='/mainmenu/'
...
```

####templates/registration/login.html
```
{% extends "base.html" %}
{% block content %}
    {% if form.errors %}
    <p>Your username and password didn't match. Please try again.</p>
    {% endif %}
    <form method="post" action="{% url django.contrib.auth.views.login %}">
    {% csrf_token %}
    <table>
        <tr>
            <td>{{ form.username.label_tag }}</td>
            <td>{{ form.username }}</td>
        </tr>
        <tr>
            <td>{{ form.password.label_tag }}</td>
            <td>{{ form.password }}</td>
        </tr>
    </table>
    <input type="submit" value="login" />
    <input type="hidden" name="next" value="{{ next }}" />
    </form>
{% endblock %}
```

####templates/base.html
```
<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="stylesheet" href="style.css" />
    <title>{% block title %}templates/base.html{% endblock %}</title>
</head>
<body>
<div id="sidebar">
    {% block sidebar %}
    <ul>
        <li><a href="/">Home</a></li>

        {% if user.is_authenticated %}
            <li><a href="/accounts/logout">Logout</a></li>
        {% else %}
            <li><a href="/accounts/login">Login</a></li>
        {% endif %}
    </ul>
    {% endblock %}
</div>
<div id="content">
    {% block content %}{% endblock %}
</div>
</body>
</html>
```

###templates/mainmenu.html
```
<!DOCTYPE html>
{% extends "base.html" %}
<html>
<head>
    <title>{% block title %}templates/mainmenu.html{% endblock %}</title>
</head>
<body>

<div id="content">
    {% block content %}
    Mainmenu
    <a href="/statinfo/">stat info</a>
    {% endblock %}

</div>

</body>
</html>
```

####templates/stat_info.html
```
<!DOCTYPE html>
{% extends "base.html" %}
<html>
<head>
    <title>{% block title %}templates/mainmenu.html{% endblock %}</title>
</head>
<body>

<div id="content">
    {% block content %}
    Mainmenu
    <a href="/statinfo/">stat info</a>
    {% endblock %}

</div>

</body>
</html>
```
