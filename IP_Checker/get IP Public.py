"""
Thanks to: http://stackoverflow.com/a/9481595
ip.42.pl
jsonip.com
httpbin.org
ipify.org
"""

from urllib2 import urlopen
my_ip = urlopen('http://ip.42.pl/raw').read()

from json import load
from urllib2 import urlopen
my_ip = load(urlopen('http://jsonip.com'))['ip']

from json import load
from urllib2 import urlopen
my_ip = load(urlopen('http://httpbin.org/ip'))['origin']

from json import load
from urllib2 import urlopen
my_ip = load(urlopen('https://api.ipify.org/?format=json'))['ip']
