"""XML TYPE
<?xml version="1.0" encoding="utf-8"?>
<rss xmlns:atom="http://www.w3.org/2005/Atom" version="2.0">
	<channel>
		<title>Q Blog</title>
		<link>http://agus.appdev.my.id/feed/</link>
		<description>Latest Posts of Q</description>
		<atom:link href="http://agus.appdev.my.id/feed/" rel="self"></atom:link>
		<language>en-us</language>
		<lastBuildDate>Mon, 29 Jun 2015 12:49:38 -0000</lastBuildDate>
		<item>
			<title>Sample Post Kapal Pesiar</title>
			<link>http://agus.appdev.my.id/entry/sample-post-kapal-pesiar</link>
			<description>Sample Post Kapal Pesiar</description>
			<guid>http://agus.appdev.my.id/entry/sample-post-kapal-pesiar</guid>
		</item>
		<item>
			<title>Test Post from user</title>
			<link>http://agus.appdev.my.id/entry/test-post-user</link>
			<description>Test Post from user</description>
			<guid>http://agus.appdev.my.id/entry/test-post-user</guid>
		</item>
	</channel>
</rss>
"""

import urllib
from bs4 import BeautifulSoup as BS

url = 'http://agus.appdev.my.id/feed/'

soup = BeautifulSoup(url)
def _getUrl_Image(url):
    start = urllib.urlopen(url)
    soup = BS(start)
    all_link = soup.findAll('item', None)
    for i in all_link:
        item = str(i)+'\n'
        split = item.split('<')
        title = split[2][6:]
        link = "<a href='"+split[4][6:]+"'>"+title+"</a>"
        print link

_getUrl_Image(url)

"""RESULT
<a href='http://agus.appdev.my.id/entry/sample-post-kapal-pesiar'>Sample Post Kapal Pesiar</a>
<a href='http://agus.appdev.my.id/entry/test-post-user'>Test Post from user</a>
"""
