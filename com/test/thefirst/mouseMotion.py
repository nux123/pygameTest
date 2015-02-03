snow_img = 'snow.gif'

import pygame
from sys import exit
from pygame.locals import *
import gameobjects
pygame.init()

snow = pygame.image.load(snow_img)
screen = pygame.display.set_mode((680,480),0,32)

clock_time = pygame.time.Clock()

x=0
y=0
speed = 250
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
   
    screen.fill((0,0,0))
    screen.blit(snow,(x,y)) 
    
    time1 = clock_time.tick()
    t = time1/1000.0
    now1 = t *speed
    x+=now1
    y+=now1
 
    if x>680 or y>480:
        x-=680
        y-=480
    pygame.display.update()   