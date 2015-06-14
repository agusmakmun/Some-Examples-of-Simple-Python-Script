import urllib2, time
from urllib2 import URLError

agent = {'User-Agent':'Mozilla/5.0'}
inp_link = raw_input("Enter Link to Click: ")

def banned(inp_link):
    request = urllib2.Request(inp_link, headers=agent)
    dump = urllib2.urlopen(request)
    #print dump.read()
    #get_title = dump[dump.find('<title>')+len('<title>'):]
    print "[+] Success", time.strftime('%D hours: %H minute: %M second: %S')
    return dump

while True:
    banned(inp_link)
