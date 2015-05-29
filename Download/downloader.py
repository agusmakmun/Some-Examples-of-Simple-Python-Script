"""
Name             : Python Downloader
Created By       : Agus Makmun (Summon Agus)
Blog             : bloggersmart.net - python.web.id
License          : GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
Documentation    : https://github.com/agusmakmun/Some-Examples-of-Simple-Python-Script/
Powered          : Ubuntu 14.04, Python 2.7 (module wget)
"""

import wget

inp = input(" [+] How Much files want to Download (ex:5)? ")
print " [+] Download file is: %s files" % inp

a = 0
tmp = []
while True:
    if inp <= inp and inp != 0:
        a += 1
        inp_url = raw_input(" [+] Paste url ke %s: " %a)
        tmp.append(inp_url)

        if a == inp:
            break
        
    else:
        print "False"

print " [+] Starting Download file..."
for i, e in enumerate(tmp):
    if i == len(tmp):
        break
    print wget.download(e)
    print " [+] Successfull..."
