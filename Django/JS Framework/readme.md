> This is an example to understand how actually Django should be work 
> with another JS Frameworks such as vuejs, angularjs, reactjs, emberjs, etc..
> if the JS Frameworks implementing similiar with syntax of `jinja2` inside `.html` templates.

**Reason of Logic Process:**

- Django => jinja {{ var }} => Output.
- Ember JS => Code {{ var }} => read as syntax of jinja => output (error).

----------------------------

> This script below is an example how to solved that problem (using emberjs).

* `templatetags/js_verbatim.py`

```python
from django import template

register = template.Library()

class VerbatimNode(template.Node):

    def __init__(self, text):
        self.text = text

    def render(self, context):
        return self.text

@register.tag
def verbatim(parser, token):
    text = []
    while 1:
        token = parser.tokens.pop(0)
        if token.contents == 'endverbatim':
            break
        if token.token_type == template.TOKEN_VAR:
            text.append('{{')
        elif token.token_type == template.TOKEN_BLOCK:
            text.append('{%')
        text.append(token.contents)
        if token.token_type == template.TOKEN_VAR:
            text.append('}}')
        elif token.token_type == template.TOKEN_BLOCK:
            if not text[-1].startswith('='):
                text[-1:-1] = [' ']
            text.append(' %}')
    return VerbatimNode(''.join(text))
```

* `templates/sample.html`

```js
{% load js_verbatim %}

<!-- Reading as Jinja syntax -->
{% for post in posts %}
   <li>{{ post.title }}</li>
{% endfor %}

<!-- Reading as syntax JS Framefork (emberjs) --->
<script type="text/x-handlebars">
    {% verbatim %}
      <section id="about_courtside" class="grid_7">
          <li>{{#link-to 'about'}}About{{/link-to}}</li>
          <li>{{#link-to 'games'}}Games{{/link-to}}</li>
      </section>
    {% endverbatim %}
</script>
```

* Refference: http://www.neckbeardrepublic.com/screencasts/ember-and-django-part-1
