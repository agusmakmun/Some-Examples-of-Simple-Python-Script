
#http://stackoverflow.com/a/189580/3445802

import urllib, urllib2, cookielib

username = 'myuser'
password = 'mypassword'

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
login_data = urllib.urlencode({'username' : username, 'j_password' : password})
opener.open('http://www.example.com/login.php', login_data)
resp = opener.open('http://www.example.com/hiddenpage.php')
print resp.read()
