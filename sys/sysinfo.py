# https://github.com/facelessuser/pymdown-extensions/blob/master/pymdownx/b64.py#L35

import sys

PY3 = sys.version_info >= (3, 0)
if PY3:
    from urllib.request import url2pathname
else:
    from urllib import url2pathname

if sys.platform.startswith('win'):
    _PLATFORM = "windows"
elif sys.platform == "darwin":
    _PLATFORM = "osx"
else:
    _PLATFORM = "linux"
