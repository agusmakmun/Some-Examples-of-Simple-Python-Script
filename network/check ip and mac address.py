agaust@agaust:~$ python
iPython 2.7.6 (default, Jun 22 2015, 18:00:18) 
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import commands
>>> commands.getoutput('ifconfig wlan0').split()[6][5:]
'192.168.1.17'
>>> commands.getoutput('ifconfig wlan0').split()[4][0:]
'2d:c0:5b:2s:91:df'
>>> 
