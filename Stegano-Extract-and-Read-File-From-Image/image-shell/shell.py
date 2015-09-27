"""
Name             : Some Examples of Simple Python Script
Created By       : Agus Makmun (Summon Agus)
Blog             : bloggersmart.net - python.web.id
License          : GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
Documentation    : https://github.com/agusmakmun/Some-Examples-of-Simple-Python-Script/
"""

import os, commands
import sys, time

username = "agus"
password = "root"

"""
$ stat <file>    --> check file information with file size include.
$ du -hs <file>  --> check file size.
"""

print "[!] Please login to access this backdoor!!"
inp_username = raw_input("[+] type username: ")
inp_password = raw_input("[+] type password: ")

def _checkMe():
    return commands.getoutput("whoami")
def _checkMac():
    return commands.getoutput("ifconfig wlan0 | grep HWaddr").split()[4]

def _checkIpWlan():
    try:
        return commands.getoutput("ifconfig wlan0 | grep 'inet addr'").split()[1][5:]
    except:
        return "This computer not connected with wlan mode."

def _checkLocation():
    return commands.getoutput("pwd")

def _checkFileDir():
    return commands.getoutput("dir").split()

def _kernel():
    return commands.getoutput("uname -a")

def _shell(command):
    return os.system(command)

if inp_username == username and inp_password == password:
    print "\n\t Welcome to simply backdoor by Summon Agus\n"
    time.sleep(1)
    print "    Checking simple information about this computer..."
    time.sleep(1)
    
    print "[+] Whoami       :", _checkMe()
    print "[+] Mac-Address  :", _checkMac()
    print "[+] IP Wlan      :", _checkIpWlan()
    print "[+] Kernel       :", _kernel()

    time.sleep(1)
    print "[+] Now checking where I am..."
    print "[+]",_checkLocation()

    time.sleep(1)
    print "[+] Checking all files with me..."
    print "[+]",_checkFileDir()

    try:
        print "[?] Are you want to work with shell ?"
        print "[?] Type CTRL+C, to exit"
        inp = raw_input("[+] Type 'yes' to woking: ")
        if inp == 'yes':
            while True:
                shell_commands = raw_input("[+] Type your command >>> ")
                _shell(shell_commands)
        else:
            print "[-] Please type 'yes' to access..."
        
    except KeyboardInterrupt:
        print "\n[-] Thank you..."
        sys.exit()
else:
    print "[!] Sorry, you are not the owner of this script"
