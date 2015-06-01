"""
Name             : Python Connect to Wifi for Linux
Created By       : Agus Makmun (Summon Agus)
Blog             : bloggersmart.net - python.web.id
License          : GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
Documentation    : https://github.com/agusmakmun/Some-Examples-of-Simple-Python-Script/
Powered          : Ubuntu 14.04, Python 2.7
"""

import os, sys

print "[+] Enter this some Option"
print " 1. Active Wifi (up)\n 2. Down Wifi (down)\n 3. Exit"
inp_up_down = raw_input("[+] Enter choice number: ")
if inp_up_down == '1':
    os.system("ifconfig wlan0 up")
    print " Are you want connect to wifi?"
    print " 1. Yes, Conncet\n 2. No, Exit"
    inp_connect = raw_input("[+] Enter your choice: ")
    if inp_connect == '1':
        os.system("iwlist wlan0 scan | grep ESSID")
        masuk = raw_input("Enter name of wifi (ex: @wifi.id): ")
        os.system("iwconfig wlan0 essid "+masuk)
        os.system("dhclient wlan0")
    elif inp_connect == '2':
	print "Thankyou.."
        sys.exit()
elif inp_up_down == '2':
    os.system("ifconfig wlan0 down")
elif inp_up_down == '3':
    sys.exit()
else:
    print "Sorry, Wrong Input!!"
