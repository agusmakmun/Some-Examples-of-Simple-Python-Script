"""
Credit: http://www.pythonlovers.net/crack-online-banking-captcha-login-using-python/
"""

from PIL import Image
import os
import time

def captcha():

    getlist = os.listdir("/home/mk/Desktop/capat/")
    number = int (len(getlist))
    for cap in range(1,number+1):
        print convert(str(cap))

def convert(cap_name):

    img = Image.open('/home/mk/Desktop/capat/'+cap_name+'.jpg')
    img = img.convert("RGB")
    pixdata = img.load()
    for y in xrange(img.size[1]):
        for x in xrange(img.size[0]):
             if pixdata[x, y][0] < 90:
                 pixdata[x, y] = (0, 0, 0, 255)
    for y in xrange(img.size[1]):
        for x in xrange(img.size[0]):
            if pixdata[x, y][1] < 136:
                pixdata[x, y] = (0, 0, 0, 255)
    for y in xrange(img.size[1]):
        for x in xrange(img.size[0]):
            if pixdata[x, y][2] > 0:
                pixdata[x, y] = (255, 255, 255, 255)
    ext = ".tif"
    img.save("/home/mk/Desktop/check/"+cap_name + ext)

    command = "tesseract -psm 7 /home/mk/Desktop/check/"+cap_name +".tif  "+"/home/mk/Desktop/text_captcha"
    os.system(command)
    time.sleep(1)

    Text = open ("/home/mk/Desktop/text_captcha.txt","r")
    decoded = Text.readline().strip('\n')
    if decoded.isdigit():
        print '[+}CAPTCHA number are ' + decoded
    else:
        print '[-] Error : Not able to decode'
captcha()
