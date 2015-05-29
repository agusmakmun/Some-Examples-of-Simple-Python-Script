"""
Name             : Python Camera with PyGame
Created By       : Agus Makmun (Summon Agus)
Blog             : bloggersmart.net - python.web.id
License          : GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
Documentation    : https://github.com/agusmakmun/Some-Examples-of-Simple-Python-Script/
Powered          : Python-2.7
"""

import pygame, sys
import pygame.camera
from pygame.locals import *

pygame.init()
pygame.camera.init()

#screen = pygame.display.set_mode((640, 480))
screen = pygame.display.set_mode((640, 480))

cam = pygame.camera.Camera("/dev/video0", (640, 480)) #webcam laptop
#cam = pygame.camera.Camera("/dev/video1", (640, 480)) #webcam usb (320, 240)
cam.start()

#image1 = pygame.image.load("masha1.png")
#image2 = pygame.image.load("masha2.png")

while 1:
    image = cam.get_image()
    screen.blit(image, (0,0))
    #screen.blit(gambar, (170,100))
    #screen.blit(gambar1, (0,0)) #image position
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
