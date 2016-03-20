* Refference: http://stackoverflow.com/a/12393845/3445802

Django has a built in groups system. Whenever you have a question like this, I recommend [searching the Django docs](https://docs.djangoproject.com/search/?q=groups&release=1), which are extensive, helpful, and well written.

So long as you are using the django.contrib.auth app, you have access to groups. You can then assign permissions to those groups.

```python
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType

content_type = ContentType.objects.get(app_label='myapp', model='BlogPost')
permission = Permission.objects.create(codename='can_publish',
                                       name='Can Publish Posts',
                                       content_type=content_type)
user = User.objects.get(username='duke_nukem')
group = Group.objects.get(name='wizard')
group.permissions.add(permission)
user.groups.add(group)
```
