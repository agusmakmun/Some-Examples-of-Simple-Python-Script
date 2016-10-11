`$ nano .pypirc`

```
[distutils]
index-servers =
    pypi

[pypi]
username:yourname
password:yourpassword
```

`$ python setup.py register -r pypi`

** Apabila terkena error:**

> Registering djipsum to https://upload.pypi.org/legacy/
> Server response (410): This API is no longer supported, instead simply upload the file.

**Maka langsung:**

`$ python setup.py sdist upload -r pypi`

* http://peterdowns.com/posts/first-time-with-pypi.html
