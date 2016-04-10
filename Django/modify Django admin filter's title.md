#### Refference:
* http://stackoverflow.com/a/21223908/3445802
* http://stackoverflow.com/a/21206760/3445802

```python
is_staff = models.BooleanField(verbose_name="My Best Staff's", default=False)
```

#### Others:

```python
from django.contrib import admin
from venom.models import Tools

def custom_titled_filter(name):
    class Wrapper(admin.FieldListFilter):
        def __new__(cls, *args, **kwargs):
            instance = admin.FieldListFilter.create(*args, **kwargs)
            instance.name = name
            return instance
    return Wrapper

class Tools_Admin(admin.ModelAdmin):
    list_display        = ('name', 'version', 'get_category', 'modified', 'created')
    list_filter         = (
                            'created',
                            ('name', custom_titled_filter('Category'))
                          )

    def get_category(self, obj):
        return obj.category.name
    get_category.short_description = 'Category'
    get_category.admin_order_field = 'category__name'

admin.site.register(Tools, Tools_Admin)
```
