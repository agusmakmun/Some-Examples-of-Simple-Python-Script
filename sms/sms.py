"""
Name             : Python SMS Sender
Created By       : Agus Makmun (Summon Agus)
Blog             : bloggersmart.net - python.web.id
License          : GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
Documentation    : https://github.com/agusmakmun/Some-Examples-of-Simple-Python-Script/
"""

import cookielib
import urllib2
import sys

sms = raw_input('[+] Enter your SMS Message: ')
no = raw_input('[+] Enter your number: ')

print '[+] In the process sending SMS....'

url ='http://www.smsgratis.web.id'
buka =  urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))
data= 'Phonenumbers='+no+'&Text='+sms+'&TOMBOL=KIRIM'

action = 'http://www.smsgratis.web.id/index.php?d=wg3&f=sms'

try:
    send = buka.open(action,data)
    req = send.read()
    send.close()

    print '[+] Congratulation...'
    print '[+] SMS wass successfull send to number : %s' % no
    print '[+] Your Message is: %s' % sms
    
except IOError:
    print '[-] Upps..! Failed send SMS.'
    sys.exit()
