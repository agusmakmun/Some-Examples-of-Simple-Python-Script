"""
Name             : Simple Spruce Filenames
Created By       : Agus Makmun (Summon Agus)
Blog             : bloggersmart.net - python.web.id
License          : GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
Documentation    : https://github.com/agusmakmun/Some-Examples-of-Simple-Python-Script/
Powered          : Ubuntu 14.04, Python-2.7
"""

import os, string
my_path = r'mypath/'

number = 0
os.chdir(my_path)
for element in os.listdir('.'):
    name_all = element [0:]
    number += 1
    string_number = str(number)
    if element in name_all:
        #print True, element
        os.rename(element, string_number+". Name of filenames.jpg")

print os.path.abspath('.')
