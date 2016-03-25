#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Name             : Money Converter using Google Finance
Created By       : Agus Makmun (Summon Agus)
Blog             : https://python.web.id
License          : GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
Documentation    : https://github.com/agusmakmun/Some-Examples-of-Simple-Python-Script/
"""

import urllib2
import time, os
from bs4 import BeautifulSoup

def money_Converter(_money, _from, _to):
    url     = ("https://www.google.com/finance/converter?a=%s&from=%s&to=%s" % (_money, _from, _to))
    agent   = {'User-Agent':'Mozilla/5.0'}
    request = urllib2.Request(url, headers=agent)
    page    = urllib2.urlopen(request).read()
    soup    = BeautifulSoup(page)
    select_ = soup.find(id="currency_converter_result")

    #eg: 0.8635 USD = 11467.2800 IDR
    return select_.text.encode('utf-8')

def get_Result_Only(converter):
    return converter.split('=')[1]

print money_Converter(1, 'USD', 'IDR')
print get_Result_Only(money_Converter(1, 'USD', 'IDR'))
