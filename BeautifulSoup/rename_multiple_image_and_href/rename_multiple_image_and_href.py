"""
Name             : Some Examples of Simple Python Script
Created By       : Agus Makmun (Summon Agus)
Blog             : bloggersmart.net - python.web.id
License          : GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
Documentation    : https://github.com/agusmakmun/Some-Examples-of-Simple-Python-Script/
"""

from bs4 import BeautifulSoup
import re

data = open("data.txt", 'r')
soup = BeautifulSoup(data.read())
result = []

href_awal = []
href_out = []
img_awal = []
img_out = []

for txt in soup.find_all(['a', 'img']):
    hreff = txt.get("href")
    imgg = txt.get("src")
    try:
        if txt.get("href")[-6:-4] == "11":
            gbr_href = hreff.replace(txt.get("href")[-6:-4], "")
            href_awal.append(hreff)
            href_out.append(gbr_href)
    except:
        if imgg is not None:
            if txt.get("src")[-6:-4] == "11":
                gbr_url = imgg.replace(txt.get("src")[-6:-4], "")
                img_awal.append(imgg)
                img_out.append(gbr_url)
data.close()

all_href = dict(zip(replace_all, href_out))
all_img = dict(zip(img_awal, img_out))

from itertools import chain
dict_chain = dict(chain(all_href.items(), all_img.items()))

def replacemany(adict, astring):
    pat = '|'.join(re.escape(s) for s in adict)
    there = re.compile(pat)

    def onerepl(mo): return adict[mo.group()]
    return there.sub(onerepl, astring)

with open("data_out.txt", 'w') as file:
    with open("data.txt", "r") as ini:
        file.write(replacemany(dict_chain, ini.read()))
