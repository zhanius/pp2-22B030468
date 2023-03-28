import pygame
from datetime import datetime
import math


#initialization
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
    
#to get current time
time = datetime.now()
sec = time.second
min = time.minute
running = True


#load. images 
clock_image = pygame.transform.scale(pygame.image.load('mickeyclock.jpeg'), (800, 600))
sechand_image = pygame.image.load('sec.png')
sechand_image = pygame.transform.scale(sechand_image, (250, 75))
sechand_rect = sechand_image.get_rect()
sechand_rect.center = (400, 300)
minhand_image = pygame.image.load('min.png')
minhand_image = pygame.transform.scale(minhand_image, (200, 50))
minhand_rect = minhand_image.get_rect()
minhand_rect.center = (400, 300)



while True:
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
            exit()
    screen.fill((0,0,0))
    screen.blit(clock_image, (0, 0))
    
    rot_minhand = pygame.transform.rotate(minhand_image, -1 * (6 * min) - 160)
    rot_minhand_rect = rot_minhand.get_rect()
    rot_minhand_rect.center = minhand_rect.center
    screen.blit(rot_minhand, rot_minhand_rect)
    
    rot_sechand = pygame.transform.rotate(sechand_image, -1 * (6 * sec) + 90)
    rot_sechand_rect =rot_sechand.get_rect()
    rot_sechand_rect.center = sechand_rect.center
    screen.blit(rot_sechand, rot_sechand_rect)

    time = datetime.now()
    sec = time.second
    min = time.minute
        
    pygame.display.update()
    clock.tick(60)
