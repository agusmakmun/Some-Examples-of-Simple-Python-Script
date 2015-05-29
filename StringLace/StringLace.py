"""
Name             : String Lace
Created By       : Agus Makmun (Summon Agus)
Blog             : bloggersmart.net - python.web.id
License          : GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
Documentation    : https://github.com/agusmakmun/Some-Examples-of-Simple-Python-Script/
Powered          : Python-2.7
"""

import string

SL = string.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz', 'CDEFGHIJKLMNOPQRSTUVWXYZABcdefghijklmnopqrstuvwxyzab')

#print string.translate("g fmmnc wms bgblr rpylqjyrc gr zw fylb", SL)
print string.translate("lyky qywy ybyjyf YESQ KYIKSL", SL)
print string.translate("nama saya adalah AGUS MAKMUN", SL)
