"""
Name             : Python Facebook Video Downloader
Created By       : Agus Makmun (Summon Agus)
Blog             : bloggersmart.net - python.web.id
License          : GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
Documentation    : https://github.com/agusmakmun/Some-Examples-of-Simple-Python-Script/
Powered          : Ubuntu 14.04, Python 2.7
"""

import urllib, re, os, sys

MAPPING = { 
    '%3D': '=',
    '%2F': '/',
    '%3A': ':',
    '%2B': '+',
    '%23': '#',
    '%3F': '?',
    '%26': '&',
}

def _initalize_url(url):
    origin_url = url
    saved = url.split('//')
    saved = saved[1].split('/')
    if saved[0][0] == 'm':
        return origin_url
    elif saved[3][0:3] == 'vb.':
        join_url = 'https://m.facebook.com/story.php?story_fbid='+saved[4]+'&id='+saved[3][3:]
        return join_url
    else:
        print "[-] Please paste link of video like this:"
        print "    https://www.facebook.com/bloggersmart/videos/vb.1455759931350973/1620030731590558/?type=2&theater"
        print "    OR:"
        print "    https://m.facebook.com/story.php?story_fbid=1620030731590558&id=1455759931350973&_rdr\n[-]"
        

def _getUrl_Video(url_video):
    start = urllib.urlopen(url_video)
    baca = start.read()
    baca = baca[baca.find('<a class="z"')+len('<a class="z"'):]
    split = baca.split('src=')
    lokasi = split[1]
    link_saved = lokasi[0:-31]
    return link_saved

def replace(match):
    return MAPPING[match.group(0)]

try:
    inp_url_video = raw_input("[+] Please Paste link video from FB: \n -> ")
    saved_initialize = _initalize_url(inp_url_video)
    url_video = _getUrl_Video(saved_initialize)
    dapat_link = re.sub('%[A-Z0-9]{2}', replace, url_video)
    
    if dapat_link[9:17] == 'fbstatic':
        print "[-] Upss sorry... you can't download this video because premission from facebook"
        print "[-] Please play before download in m.facebook.com/id_video"
        sys.exit()
    else:
        pass
    
    print "[+] Your Links download of video:\n--------------------------\n", dapat_link, "\n--------------------------"
    print "[+] Starting download file..."
    print "[+] Your saved video is: my_video.mp4"
    os.system('wget "'+dapat_link+'" -O my_video.mp4')
    print os.listdir('.')
    sys.exit()
except Exception:
    print "[-] Lost Connection"
