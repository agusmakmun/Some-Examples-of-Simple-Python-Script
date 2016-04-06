* https://docs.djangoproject.com/en/1.9/_modules/django/contrib/auth/decorators/#login_required
* http://stackoverflow.com/a/32331657/3445802

```python
from functools import wraps

def profile_required(view_func):
  def _decorator(request, *args, **kwargs):
    if request.user.is_anonymous():
        return redirect(LOGIN_URL)
    else:
        try:
            profile = Profile.object.get(user=request.user)
        except Profile.DoesNotExist:
            return redirect('userprofile_url')

    response = view_func(request, *args, **kwargs)

    return response
return wraps(view_func)(_decorator)


@profile_required
def your_func(request):
   # do something
```
