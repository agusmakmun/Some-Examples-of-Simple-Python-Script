This `configparser` python3 module is verry usefull if you need 
to read your configuration, such as: site.conf, foo.ini, or else.

* **DOCS**: https://docs.python.org/3.5/library/configparser.html

Example, inside file of `accounts.conf`:

```
[github.com]
username=john
email=john@site.com
phone=0213940193

[bitbucket.com]
username=alex
email=alex@site2.com
phone=0003919319
```

=============================================

```python
>>> import configparser
>>> conf = configparser.ConfigParser()
>>> conf.sections()
[]
>>> conf.read('accounts.conf')
['test.conf']
>>> conf.sections()
['test.conf']
>>> 'github.com' in conf
True
>>> conf['github.com']['username']
'john'
>>> conf['github.com']['email']
'john@site.com'
>>> conf['github.com']['phone']
'0213940193'
>>>
```
