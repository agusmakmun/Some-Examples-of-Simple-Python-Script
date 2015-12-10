import urllib, urllib2, cookielib

username = 'username'
password = 'password'

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
login_data = urllib.urlencode({'session[username_or_email]' : username, 'session[password]' : password})
opener.open('https://twitter.com/sessions', login_data)
resp = opener.open('https://twitter.com/yourname')
op = open("out_twitter.txt", "w")
op.write(resp.read())
op.close()
