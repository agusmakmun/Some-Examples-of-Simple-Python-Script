"""
1. Download Wvdial: http://ftp.us.debian.org/debian/pool/main/w/wvdial/
2. cd /Download/
3. sudo dpkg -i *.deb
4. lsusb
5. lsusb -v -d 12d1:1506   --> go to check idVendor and idProduct
6. python wvdial.py
... 1. Connect
... 2. Setting    ---> cukup setting di bagian setting = dibawah 

[ Note ]
Baud = 460800   ---> baud rate, tergantung modem
"""

"""
Name             : Python Wvdial
Created By       : Agus Makmun (Summon Agus)
Blog             : bloggersmart.net - python.web.id
License          : GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
Documentation    : https://github.com/agusmakmun/Some-Examples-of-Simple-Python-Script/
"""

import os, sys
idVendor = '0x12d1'
idProduct = '0x1506'
path = '/etc/wvdial.conf'
setting = """
[Dialer indosat]
Init1 = ATZ
Init3 = AT+CGDCONT=1,"IP","internet"
Modem Type = USB Modem
ISDN = 0
Baud = 460800
New PPPD = yes
Modem = /dev/ttyUSB0
Phone = *99#
Modem = /dev/ttyUSB0
Username = off
Password = off
Stupid mode = 1
Auto DNS = off
"""


class WvDial(object):
    def _connect(self, idVendor, idProduct):
        os.system("modprobe usbserial vendor="+idVendor+" product="+idProduct)
        os.system("wvdial indosat")

    def _setting(self):
        op = open(path, 'w')
        op.write(setting)
        op.close()
        
    def _checkRoot(self):
        if os.getuid() != 0:
            print "[-] Please Access as root..!"
            sys.exit()
        else:
            pass
    

if __name__ == "__main__":
    mome = WvDial()
    mome._checkRoot()
    print "Pilihan Setting: \n 1. Connect\n 2. Setting"
    inp_usr = raw_input("Masukkan Pilihan: ")
    if inp_usr == '1':
        mome._connect(idVendor, idProduct)

    elif inp_usr == '2':
        mome._setting()

    else:
        pass
    



