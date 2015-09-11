"""
$ sudo apt-get install python-socksipy
$ sudo apt-get install tor
$ sudo service tor restart

# setting your browser like this: http://i.imgur.com/2aHruSC.png
# https://www.youtube.com/watch?v=KDsmVH7eJCs
# https://www.youtube.com/watch?v=3p-buQT72u0
# http://my-ip.herokuapp.com

>>> import httplib
>>> conn = httplib.HTTPConnection("my-ip.herokuapp.com")
>>> conn.request("GET", "/")
>>> res = conn.getresponse()
>>> res.read()
'{\n  "ip": "180.252.181.92"\n}'
>>> 
"""

import os, sys, time, httplib
import socket, socks
import urllib, urllib2

port = 9050
ip = 'my-ip.heroku.com'

class _TOR(object):
    port       = 9050
    new_port   = 9050 #change to 9051, but isn't work.
    ip         = "my-ip.heroku.com"
    localhost  = "127.0.0.1"
        
    def _checkRoot(self):
        if os.getuid() != 0:
            print "[-] Please Access as root..!"
            sys.exit()
        else:
            pass
        
    def _connectTOR(self):
        socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, self.localhost, self.port, True)
        socket.socket = socks.socksocket

    def _newIdentity(self):
        socks.setdefaultproxy()
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.localhost, self.new_port))
        s.send("AUTHENTICATE\r\n")

        self.response = s.recv(128)
        
        if self.response.startswith("250"):
            s.send("SIGNAL NEWNYM\r\n")
        s.close()

        _TOR()._connectTOR()
        
    def main(self):
        os.system('sudo service tor restart')
        _TOR()._connectTOR()
        
        print " * Connected to TOR..."
        time.sleep(1)
        print " * Please wait.. now checking your IP..."
        
        conn = httplib.HTTPConnection(self.ip)
        conn.request("GET", "/")
        response = conn.getresponse()
        #print response.status, response.reason
        #print (response.read())
        
        f =  urllib2.urlopen("http://"+self.ip)
        print f.read()

        _TOR()._newIdentity()

        conn = httplib.HTTPConnection(self.ip)
        conn.request("GET", "/")
        response = conn.getresponse()
        #print response.status, response.reason
        print (response.read())
        
        
if __name__ == "__main__":
    _TOR()._checkRoot()
    print " 1 > Ready to start TOR\n 2 > Stop the TOR"
    _inpUsr = raw_input("___Enter your choice >> ")
    if _inpUsr == '1':
        _TOR().main()
    elif _inpUsr == '2':
        os.system('sudo service tor stop')

