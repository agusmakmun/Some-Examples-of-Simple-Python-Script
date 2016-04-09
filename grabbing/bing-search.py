__author__ = 'Ted Maxwell'
"""
This is my first python project, I seen a lot of web crawlers with big code in them why to do that just made this project with bit of knowledge I had of Python it worked on my Win7x86 Pycharm Py3.5 properly but not in Kali. 
"""
import requests
from bs4 import BeautifulSoup

def core(url):
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    for link in soup.findAll('li',{"class":"b_algo"}):
        linkheader = link.h2.a
        rawtitle = str(link.h2.a)
        title = rawtitle.replace('<strong>',"").replace('</strong>',"").replace('</a>','').replace('<a','')
        indexOf = title.index('>') + 1
        if not("Images for " + inputt in rawtitle) or not("Videos of " + inputt in rawtitle):
            print(title[indexOf:] + "\n" + linkheader.get("href") + "\n")
pgno = 1
inputt = input("Bing Search:\n")
address = inputt.strip().replace(' ','+')
bool = True

while bool:
    url = "https://www.bing.com/search?q=" + address + "&first=" + str(pgno)
    pgno += 10
    core(url)
    if input("Press Enter To Crawl Next Page") != "":
        bool = False
    else:
        print("\n\n::::::::::::::::::::: Page ",((pgno-1)//10)+1,"::::::::::::::::::::::::\n\n")
