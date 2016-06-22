# -*- coding: utf-8 -*-

''' Created by: Summon Agus (agus@python.web.id)
    Licensed  : MIT '''

import os, sys, urllib, urllib2
from bs4 import BeautifulSoup

path_download_images = 'images/'

if os.path.isdir(path_download_images) == False:
    os.makedirs(path_download_images)

def downloadImages(url):
    page   = BeautifulSoup(urllib2.urlopen(url))
    images = [ img['src'] for img in page.findAll('img') ]
    
    print '[i] Downloading {} images...'.format(len(images))
    count = 0
    for image in images:
        count += 1
        name = image.split('/')[-1]
        urllib.urlretrieve(image, path_download_images + name)
        print ' {}. Downloaded `{}`'.format(count, name)

    print '[i] Success downloaded {} images to path `{}`'.format(count, path_download_images)

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print './{} [url]'.format(__file__)
    else:
        downloadImages(sys.argv[1])
