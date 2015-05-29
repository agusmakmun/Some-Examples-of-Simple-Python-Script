"""
Name             : Ip Checker
Created By       : Agus Makmun (Summon Agus)
Blog             : bloggersmart.net - python.web.id
License          : GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
Documentation    : https://github.com/agusmakmun/Some-Examples-of-Simple-Python-Script/
Powered          : Ubuntu, Python-2.7
"""

import subprocess

print '\n\tWelcome to Lookup domain IP\n\tCtrl+C to Exit..'
def looking():
    while True:
        try:
            inp = raw_input(" [+] Enter Domain Name: ")
            out = open('domain.txt', 'w')
            subprocess.call(['ping', '-c 1', inp], stdout = out)
            out.close()

            data = open('domain.txt', 'r')
            op = data.readline()
            pisah = op.split()
            print " [+] Ip domain is     :",pisah[2].replace('(','').replace(')',''), "\n"

        except KeyboardInterrupt:
            print "\n\tThank you.."
            break

looking()


'''
import os
command = os.system('ping 127.0.0.1 >> new.txt')
'''
