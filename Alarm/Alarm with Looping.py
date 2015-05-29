"""
Name             : Alarm with Looping
Created By       : Agus Makmun (Summon Agus)
Blog             : bloggersmart.net - python.web.id
License          : GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
Documentation    : https://github.com/agusmakmun/Some-Examples-of-Simple-Python-Script/
Powered          : Python-2.7, mpg321

[+]--- use ---[+]
$sudo apt-get install mpg321
$python Alarm\ with\ Looping.py
"""

import os, time

minute = 60
hourse = minute * minute

print 'Alarm dalam 1 Jam..'
while True:
    time.sleep(hourse) #change this optioal time
    os.system('mpg321 rest_alert.mp3')
