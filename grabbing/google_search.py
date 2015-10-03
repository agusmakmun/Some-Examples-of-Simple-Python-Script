"""
Name             : Some Examples of Simple Python Script
Created By       : Agus Makmun (Summon Agus)
Blog             : bloggersmart.net - python.web.id
License          : GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
Documentation    : https://github.com/agusmakmun/Some-Examples-of-Simple-Python-Script/
"""

import time
import mechanize
from bs4 import BeautifulSoup

print """
\t// Welcome to Python search engine Google
\t// Simple Application to get result search from { query }
\t// Design by: Summon Agus - github.com/agusmakmun
\t// Thanks to: cyroxx - http://stackoverflow.com/a/16020863
"""
query = raw_input("[+] Type your query: ")

#prepare mechanize
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_equiv(False)
br.addheaders = [('User-agent', 'Mozilla/5.0')] 
br.open('http://www.google.com/')

# do the query
br.select_form(name='f')   # Note: select the form named 'f' here
br.form['q'] = query
data = br.submit()
soup = BeautifulSoup(data.read())

print "[+] Result query of %s ...\n" % query
count = 0
numb  = 0
for post in soup.select('li.g'):
    count += 1
    numb  += 1
    get_link     = post.find('a', href=True)
    href         = get_link['href']
    link_result  = href[7:].split("&sa")[0]

    get_title    = str(get_link).split('">')[1]    
    get_remove   = get_title.replace('<b>','').replace('</b>','').replace('</a>','')\
                   .replace('&amp;', '&').replace('...','')
    title_result = get_remove
    time.sleep(1)
    
    if link_result[0:3] == '?q=':
        count -= 1
        numb -= 1
    else:
        print [ numb ], title_result
        print [ count ], link_result
        print "---------------------------"
        
