```html
{% if request.user.groups.all.0.name == 'Authors' %}
    <p>Tampilkan Avatar</b>
{% else %}Kosongkan avatar
{% endif %}
```
