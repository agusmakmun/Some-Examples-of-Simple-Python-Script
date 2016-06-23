# -*- coding: utf-8 -*-

''' Created by: Summon Agus (agus@python.web.id) at Wed, 22 Jun 2016 : 20:50
    Licensed  : MIT '''

import os, sys, urllib, urllib2
from bs4 import BeautifulSoup

path_download_images = 'images/'

if os.path.isdir(path_download_images) == False:
    os.makedirs(path_download_images)

def downloadImages(url):
    page   = BeautifulSoup(urllib2.urlopen(url))
    images = set([ img['src'] for img in page.findAll('img') ])
    
    print '[i] Downloading {} images...'.format(len(images))
    count = 0
    for image in images:
        name = image.split('/')[-1].replace('%20', ' ')
        try:
            count += 1
            urllib.urlretrieve(image, path_download_images + name)
        except:
            count -= 1
            continue
        print ' {}. Downloaded `{}`'.format(count, name)

    print '[i] Success downloaded {} images to path `{}`'.format(count, path_download_images)

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print './{} [url]'.format(__file__)
    else:
        downloadImages(sys.argv[1])
