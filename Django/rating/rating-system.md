> This is sample rating system use module from `django-updown` (https://github.com/weluse/django-updown/), and with ajax method. This available on my tutorial: https://python.web.id/blog/implement-ajax-vote-ratings-with-django-updown/

##### 1. Install the module

```shell
$ pip install django-updown
```

##### 2. Cofiguration in `settings.py`

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    ...
    
    'your_app',
    'updown',
]
```

##### 3. Register to `your_app/models.py`

```python
from __future__ import unicode_literals
from django.db import models
from updown.fields import RatingField

class Tutorial(models.Model):
    title   = models.CharField(max_length=200)
    slug    = models.SlugField(max_length=200, unique=True)
    ...
    rating  = RatingField(can_change_vote=True)

```

##### 4. If you need showing the ratings inside your admin. in your `your_app/admin.py`

```python
from your_app.models import Tutorial
from updown.models import Vote

admin.site.register(Tutorial)
admin.site.register(Vote)
```

##### 5. Add the url in `your_app/urls.py`

```python
from django.conf.urls import include, url
from updown.views import AddRatingFromModel

urlpatterns = [
    url(r"^tutorial/(?P<object_id>\d+)/rate/(?P<score>[\d\-]+)$", AddRatingFromModel(), {
        'app_label': 'your_app', #app_label is in `INSTALLED_APPS`
        'model': 'Tutorial',
        'field_name': 'rating',
    }, name="vote_rating"),
]
```

##### 6. In your templates single page for tutorial, ex: `your_app/templates/single.html`

```html
{% include "base.html" %}

{% block content %}
<div class="rating">
  <style type="text/css">
    .rating {float: right;}
    .rating button {border-radius: 20px;padding: 10px;border: 1px solid #fff;box-shadow: 1px 1px 2px #C3C0C0;}
    .total-likes {float: left;margin: 0 10px;width: 150px;padding: 8px 10px;font-weight: bold;border-radius: 5px;border: 1px solid #EEEEEE;box-shadow: 2px 2px 2px #f0f0f0;}
    .modal-dialog {top: 5em;}
    .modal-content {box-shadow: 0 3px 10px rgba(0, 0, 0, 0.14);border: 1px solid #ddd;}
    #result {margin: 0 auto;text-align: center;}
  </style>

  <div class="total-likes">
    Total likes: <span>{{ object.rating.likes }}</span>
  </div>

  <button class="btn btn-lg btn-success" id="submit-vote-up">
    <i class="fa fa-thumbs-up" aria-hidden="true"></i>
  </button>

  <button class="btn btn-lg btn-danger" id="submit-vote-down">
    <i class="fa fa-thumbs-down" aria-hidden="true"></i>
  </button>

  <!-- posisi ini jika si jquery dan js-bootstrap tidak berada di atas, maka function tidak berfungsi -->
  <script type="text/javascript" src="/static/js/jquery-2.2.2.min.js"></script>
  <script type="text/javascript" src="/static/js/bootstrap.min.js"></script>

  <script>
      function responseSuccessMessage(success) {
          $('#myModal').show();
          $("#result").html(success);
          setTimeout(function(){
              $("#myModal").hide(10);
          }, 1000);
      }
      function responseErrorMessage(error) {
          $('#myModal').show();
          $("#result").html(error.responseText);
          setTimeout(function(){
              $("#myModal").hide(10);
          }, 1000);
      }

      $(document).ready(function(){
          $("#submit-vote-up").click(function(){
              $.ajax({
                      type: "GET",
                      url: "{% url 'vote_rating' object_id=object.pk score=1 %}",
                      success: function(result){
                        return responseSuccessMessage(result);
                      },
                      error: function(rs, e) {
                        return responseErrorMessage(rs);
                      }
              });
          });
          $("#submit-vote-down").click(function(){
              $.ajax({
                      type: "GET",
                      url: "{% url 'vote_rating' object_id=object.pk score=-1 %}",
                      success: function(result){
                        return responseSuccessMessage(result);
                      },
                      error: function(rs, e) {
                        return responseErrorMessage(rs);
                      }
              });
          });
      });
  </script>

  <div id="myModal" class="modal fade in" tabindex="-1" role="dialog">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-body">
          <p id="result"></p>
        </div>
      </div>
    </div>
  </div><!-- end #myModal, modal for response message -->
</div><!-- end rating -->

{% endblock %}
```
